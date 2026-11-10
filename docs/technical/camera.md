# Interne Kameras: Boardvertrag vor Treiberaktivierung

Gültig für **Lenovo Yoga Pro 9 15N1X11, Typ 83SR, ARM64**.
Zur Einordnung: [Hauptanleitung](../guide.md) · [Status](../status.md).

**Stand der ausgewerteten Evidenz: 10. November 2026. Kein funktionierender Kamera-Capture ist nachgewiesen; `ready_to_load=false`.** Die Untersuchungen grenzen GPIO-, Clock- und Transportverträge ein. Sie beweisen weder einen physisch anliegenden Sensortakt noch eine sichere Versorgung oder einen Bilddatenstrom. Diese Seite enthält keine aktive Probe-, GPIO- oder Registeranleitung.

## Identität und Pipeline

Die Zuordnung stammt aus gespeicherter ACPI-Evidenz und abschnittsbezogenen Windows-INF-Einträgen für dieses Modell, nicht aus einem neuen Sensor-Chip-ID-Lesezugriff.

| Funktion | ACPI-/Metadatenkennung | Aussagegrenze |
|---|---|---|
| Frontkamera `CAMF` | `NVDA2810`, Subsystem `MDK0000`; `ov08x40_mipi_raw` | Konfigurierter Sensor **OV08X40**, CSI-Port 0 laut Paketmetadaten |
| IR-Kamera `CAMI` | `NVDA2812`, Subsystem `MDK0002`; `vd55g0_mipi_raw` | Konfigurierter Sensor **VD55G0**, CSI-Port 2 laut Paketmetadaten |
| Sensorinterface `SENI` | `NVDA2820` | SENINF-/CSI-Empfangspfad, kein eigenständiger Sensornachweis |
| Kamerasteuerung `CCU0` | `NVDA2808` | CCU-Steuerung und Firmwareabhängigkeit |
| Bildverarbeitung `ISP1` | `NVDA2801` | Weitere Stufe der Kamera-Pipeline |
| GPIO-Controller `GIO0` | `NVDA9221`, gespeicherter `ChipId=1` | Geprüfte Registergeometrie und Ressourcenverwaltung, kein Schaltplan |

Der vollständige Pfad benötigt Sensorversorgung und Reset → realen XVCLK → alleinigen Sensorowner → CSI-/SENINF-/PHY-Konfiguration → CCU-/Firmwarevertrag → Media-Graph → Capture-DMA/IOMMU → Bildabnahme. Ein erkannter ACPI-Knoten, ein gebautes Media-Modul oder ein vorhandener Graph überspringt keine dieser Stufen.

## Reproduzierbare Untersuchungsfolge

1. **Metadaten sauber trennen:** Gespeicherte ACPI-Ressourcen und passende INF-Installationsabschnitte zusammenführen. Ein Sensorname irgendwo im Paket reicht nicht; Front- und IR-Einstellungen dürfen nicht vermischt werden.
2. **Eingänge festlegen:** DSDT, ARM64-Treiberdateien, öffentliche Quellschnappschüsse und ABI-Header gegen Manifeste prüfen. PE-Dateien nur statisch lesen; Datei-Offsets, RVA und virtuelle Adressen nicht gleichsetzen.
3. **Verbraucher und Anbieter verfolgen:** Von Sensorsequenzen über Namen und ConnectionIds bis zum tatsächlich konstruierten GPIO- bzw. Clock-Auftrag gehen. Aufgerufene WDF-Schnittstellen mit dem passenden Header abgleichen. Datenkopie, Submission, Completion und physische Wirkung getrennt behandeln.
4. **Ausführbare Offline-Verträge bauen:** Instruktionsanker, Tabellenlayouts, Endianness, Grenzwerte und Fehlerpfade prüfen. Mutationen müssen den Prüfer scheitern lassen. Das ist statische Regression mit lokalen Modellen, keine Ausführung oder Emulation eines Kameratreibers.
5. **Erst dann Linux-Integration beurteilen:** Ein gebooteter Diagnosekernel stellt Infrastruktur bereit, aber keinen fertigen Boardport. Eine Umsetzung benötigt einen belegten Power-/Clockprovider, genau einen Sensorowner und geprüfte Fehler-/PM-Pfade.

Die internen Fortsetzungen erhalten frühere Artefakte per Hashvergleich. Wiederholungen müssen in einer eigenen Review-Arbeitskopie erfolgen, wenn die Prüfer Berichte regenerieren. Diese Dokumentation liefert bewusst weder die privaten Eingänge noch die ausführbaren Prüfpakete mit.

## Was die bisherigen Fortsetzungen tatsächlich schließen

### Transport ist nicht Sensortakt — Fortsetzung v2

Der eigene gespeicherte Camsys-Treiber erlaubt die Rekonstruktion eines Mailboxpfads: Belegtprüfung, Datenkopie, Signalisierung, anschließend ein getrenntes Warten mit zusätzlicher Statusprüfung. Eine abgeschickte oder softwareseitig abgeschlossene Nachricht beweist keine elektrische Clockwirkung. Strukturell ähnliche Nachrichten ersetzen keine boardspezifische ID-/Raten-/Ownersemantik.

Die Quellprüfung trennt außerdem direkte Sensorprogrammierung und einen lediglich beschriebenen Sensor-Subdevice-Knoten. Ein Media-Graph allein beweist keine Bindung des nativen OV08X40-Treibers. Zwei parallele Sensorowner sind keine zulässige Integrationsabkürzung.

### GPIO-Anbieter — Fortsetzung v3

Der gespeicherte GPIO-Treiber wählt anhand der eigenen ACPI-Chipkennung ein Registerlayout. MODE-, Richtungs-, Eingangs- und Ausgangsgeometrie wurden gegen die entsprechende MT8901-Linux-Implementierung abgeglichen. Die tatsächliche Callbackregistrierung und die lokale Schreibsemantik wurden geprüft.

Die Bedeutung ist begrenzt: Eine rechnerisch bestimmte Registerposition ist **keine Registermessung**. Eine vorhandene alternative Pinmuxfunktion ist **kein Nachweis einer laufenden Clockleitung**. Lokale Ausgangspegel beweisen keine unveränderte Polarität bis zum Sensor.

### GPIO-Verbraucher — Fortsetzung v4

Die statische Kette ist nun Name → Index → gefilterte GPIO-I/O-ConnectionId → Resource-Hub-Open → Schreibrequest. Sie schließt die frühere Lücke zwischen bloß parallelen Ressourcenlisten und tatsächlich verwendeter Consumerregel.

| Gerät | Name | GPIO-Ressourcenindex | ACPI-Pin |
|---|---|---:|---:|
| CAMF | `campower` | 0 | 34 |
| CAMF | `reset` | 1 | 39 |
| CAMI | `campower` | 0 | 102 |
| CAMI | `reset` | 1 | 95 |

Diese Pins sind Controllerressourcen, keine physisch vermessenen Sensornetze. Der gespeicherte Frontkameraablauf fordert Reset zunächst als 0, später als 1 und `campower` als 1 an. Die getrennten On-/Off-Werte und Verzögerungen wurden anhand der echten Consumerfelder geprüft; die Verzögerungseinheit dieses Pfads ist Millisekunden. Die rückwärts laufende Off-Schleife lässt Eintrag 0 aus.

Daraus darf **kein** geratenes `GPIO_ACTIVE_LOW`-/`GPIO_ACTIVE_HIGH`-Binding entstehen. Externe Invertierung, Railzuordnung, weitere Callbacks, Fehlerbehandlung und gemeinsame IR-Ressourcen sind damit nicht vollständig belegt. Ein beobachteter erfolgreicher Windows-Open oder elektrischer Start wurde nicht aufgezeichnet.

### Auxiliary-Pfad und Clock-Gates — Fortsetzung v5

Eine alternative Sensoroperation führt zu einem IR-spezifischen Hilfsziel namens `irled` bzw. `lens`. Sie ist kein nachgewiesener XVCLK-Aufruf. Die Bedeutung des angeschlossenen Hilfsbausteins ist nicht vollständig rekonstruiert; feste Schreibbytes werden deshalb nicht zu Clockprogrammierung umgedeutet.

CCU und SENINF konstruieren außerdem Bulk-Clockanforderungen, die Camsys als Typ-2-Mailboxauftrag serialisiert. Die dabei belegten logischen Provider-IDs identifizieren noch keinen physischen Sensorclock-Ausgang. Enable/Disable-Paketbau ist weder Rail-Stabilität noch Gate-/PM-Ownership.

### Rate-ABI und Präzision — Fortsetzung v6

Der getrennte SENINF-Ratepfad übergibt ein ID-/Ratenpaar und erzeugt einen Typ-3-Mailboxauftrag. Die statisch geprüfte Sender-/Providerkette skaliert nominell Tabellen-MHz → IOCTL-Hz → **Ganzzahl-MHz**. Die Providerdivision wurde über die vollständigen u32-Quotientenintervalle geprüft.

Eine anfängliche kHz-Hypothese wurde durch echte Tests verworfen und bleibt als Fehlversuch erhalten. Der korrigierte Offline-Serializer verweigert nicht exakt darstellbare Raten statt zu runden. Insbesondere liefert diese Ganzzahlschnittstelle **keinen Beleg für 19,2 MHz am Sensor**. Sie schließt einen nachgeschalteten Teiler, einen festen Oszillator oder einen anderen Firmwarepfad nicht aus. Weder untersuchte ID-Auswahlzweige noch synthetische Testwerte identifizieren die physische XVCLK-Leitung.

Der unabhängige Parent-Review reproduzierte sieben v6-Tests einschließlich Anker-Mutationen und Quotientenintervallgrenzen. Das ist Bestätigung des ABI-Modells, keine Kamera-Hardwarefreigabe.

### GPIO-Ausgangsverantwortung — Fortsetzung v7

Die folgende statische Providerprüfung schließt eine zuvor offene Bedingung: Der untersuchte Output-Zweig fordert **DIR=1 und MUX=0** an. Die vier gespeicherten Kamera-GPIO-Ressourcen besitzen keine VendorData; der alternative Mux-Override dieses Pfads greift dort deshalb nicht. Der registrierte `DisconnectIoPins`-Callback kehrt lokal nur erfolgreich zurück und stellt selbst keine Clock-Muxfunktion wieder her.

Damit lassen sich CAMF-Pin 34 (`CMMCLK4`) und Pin 39 (`CMMCLK0`) **während des verfolgten GPIO-Ownership-Intervalls nicht als XVCLK-Ausgänge begründen**. Diese Aussage ist bedingt auf den untersuchten Providerpfad; sie beweist weder die physische Verdrahtung noch das dauerhafte Ausbleiben eines Takts oder das Verhalten sämtlicher anderer Owner.

Ein ausführbarer Offline-Vertragsprüfer kontrolliert echte ARM64-Instruktionsanker, AML-Ressourcen und ABI-/Quelllayouts. Seine Negativtests verändern auch AML-Inhalte mit neu berechneter gültiger Prüfsumme; ein syntaktisch intakter ACPI-Container genügt somit nicht als semantischer Nachweis. Ein zusätzlicher Offline-Guard verweigert dazu widersprüchliche Pinmuxpläne. Das versiegelte neue Paket wurde auf Integrität geprüft; eine unabhängige Wiederholung der neuen Tests steht noch aus. Es gibt weiterhin **keine Runtime-Clockimplementierung und keine Hardwareaktivierung**.

## Aktuelle Grenzen

- **XVCLK bleibt die kleinste offene physische Kante:** Sensoreingang → Boardnetz/Mux oder Oszillator → tatsächlicher Anbieter, gegebenenfalls mit Parent, Teilern, Ratenkodierung, Gate, Completion und PM-/Ownervertrag.
- Der untersuchte Linux-OV08X40-Treiber fordert **19,2 MHz**. Das ist eine Treiberanforderung, keine Yoga-Messung. Ein Rohbyte oder plausibler Taktwert rechtfertigt weder einen Dummyclock noch das Entfernen dieses Guards. Ein abweichender belegter Eingangstakt benötigt konsistente PLL-/Modusänderungen.
- `campower` benennt keine bewiesene AVDD-/DVDD-/DOVDD-Zuordnung. Physischer Resetpegel, Spannungen, Einschwingzeiten und vollständige Ein-/Ausschaltreihenfolge bleiben offen.
- Elektrische Lanezuordnung, PHY-, CCU-/Firmware- und Receiververtrag sowie DMA-/IOMMU-Stillstand und Fehlerabwicklung sind separat offen.
- Eine Strukturprüfung eines Firmwarecontainers beweist weder Signaturgültigkeit noch RPC-Kompatibilität oder erfolgreichen CCU-Start.
- Es existiert kein akzeptierter Bilddatenstrom. Auch eine erfolgte Diagnosekernelinstallation oder ein erfolgreicher Boot wäre nur Infrastrukturbeleg, nicht Kameraabnahme.

Die bisherigen Suchergebnisse sind auf tatsächlich geprüfte Quellen begrenzt. Sie beweisen nicht, dass passende Herstellerunterlagen grundsätzlich nicht existieren. Neue Offline-Erkenntnisse erlauben keinen Blindport oder Force-bind.

## Nächste Akzeptanzkriterien

1. **Boardvertrag beschaffen:** Für genau 83SR die XVCLK-Netz-/Quellenzuordnung und Versorgung/Reset einschließlich Polarität, Reihenfolge und gemeinsamer Owner nachweisen. Bei programmierbarem Clockpfad ID, Parent, Teiler, Rate und Ein-/Ausschaltsemantik belegen. Eine Liste logischer IDs genügt nicht.
2. **Werte physisch einordnen:** Herstellerunterlagen oder eine separat begründete und autorisierte passive Messung müssen tatsächlichen Sensortakt und zeitliche Pegelbeziehungen belegen. Eine Messung allein ersetzt noch keinen Linux-Ownershipvertrag. Solche Messungen sind hier nicht durchgeführt worden.
3. **Implementierung unabhängig prüfen:** Reale Clock-/Powerprovider, genau einen Sensorowner, passende Sensor-/PLL-/Modusdaten und Receiverkonfiguration entwickeln. Probe, Abbruch, Streamende und PM-/Unwind-Fehler müssen Ressourcen geordnet zurückgeben; keine bloßen Erfolgsmeldungen anstelle echter Operationen.
4. **Hardware getrennt abnehmen:** Erst eine geprüfte begrenzte Initialisierung, dann tatsächlichen Sensoridentitätsnachweis, Media-Links und schließlich gültige Frames mit definiertem Format, Abmessungen, Zeitstempeln und begrenzter Laufdauer nachweisen. DMA-/IOMMU- und Kernelmeldungen sowie sauberes Streamende mitbewerten. Front- und IR-Pfad jeweils separat akzeptieren; ein Erfolg überträgt sich nicht automatisch.

Bis dahin bleibt `ready_to_load=false`. Kein GPIO-Schreiben, I²C-Scan, Clock-Erraten oder Treiberladen folgt aus dieser Dokumentation.

## Herkunft und Veröffentlichungsgrenze

Ausgewertet wurden folgende **logischen internen Artefaktnamen**, nicht im Repository enthalten:

- `camera-preflight/yoga-acpi-device-summary.json`
- `camera-preflight/driverstore-camera-summary.json` mit abschnittsbezogenen Sensor-/Portangaben
- `camera-preflight/continuation-v2/FINDINGS.md`
- `camera-preflight/continuation-v3/FINDINGS.md`
- `camera-preflight/continuation-v4/FINDINGS.md`
- `camera-preflight/continuation-v5/FINDINGS.md`
- `camera-preflight/continuation-v6/FINDINGS.md`
- `camera-preflight/continuation-v7/FINDINGS.md` und `NEXT-PORTING-DELTA.md` (neuer Abschluss, Integrität geprüft; vollständige unabhängige Testwiederholung noch offen)
- `audio-next-kernel/afe-functional-irq-parent-review-v1/PARENT-REVIEW.md`, Abschnitt zur unabhängigen v6-Prüfung

Die internen Berichte binden Eingänge, öffentliche Quellschnappschüsse und Regressionen an feste Inhalte. **Diese Beweiskette ist aus dem öffentlichen Repository noch nicht unabhängig reproduzierbar.** Hier werden weder private Rohprotokolle noch Disassemblies, Treiberbinärdateien, Firmware oder aktivierende Patches veröffentlicht. Der technische Status bleibt ausdrücklich: rekonstruierte Teilverträge, aber keine funktionierende Kamera.
