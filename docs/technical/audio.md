# Internes Audio: Treiberkette, Nachweise und offene Grenzen

Gültig für **Lenovo Yoga Pro 9 15N1X11, Typ 83SR, ARM64**.
Zur Einordnung: [Hauptanleitung](../guide.md) · [Status](../status.md).

**Stand der ausgewerteten Evidenz: 10. November 2026. Internes Audio ist nicht als funktionsfähig nachgewiesen.** Eine reale ALSA-Karte wurde unter bewusst eingeschränkten Bedingungen registriert. Sie besitzt keinen neuen Benutzer-PCM; es gab weder Wiedergabe noch hörbaren Lautsprecherton. Diese Seite ist eine technische Bestandsaufnahme, keine Lade- oder Wiedergabeanleitung.

## Hardware und notwendige Kette

| Ebene | Identität bzw. Aufgabe |
|---|---|
| SoundWire-Controller | ACPI `NVDA9100`, untersuchter Backend-DAI `SDW1_Playback3` |
| Audio Front End (AFE) | ACPI `NVDA9022`, downstream MT8901-Code; künftig DMA, Takte, Power Management und PCM |
| Codec | Cirrus Logic **CS42L43**, SoundWire und MFD-/Codec-Untergeräte |
| Lautsprecherverstärker | Zwei **CS35L56**, SoundWire-UID 0 und 1; Firmware und gerätespezifische Koeffizienten erforderlich |
| Boardzuordnung | Subsystemkennung `17aa3805`; Lautsprecherauswahl über `SdwSpeaker` |
| Vollständiger Audiopfad | Controller → Transport → Codec/Verstärker → AFE und Machine-/DAPM-Routing → PCM → Audio-Userspace |

Eine vorhandene ACPI-ID beweist keinen gebundenen Treiber. Ein gebundener Codec beweist weder sichere Verstärkerversorgung noch funktionierende DMA. Eine ALSA-Karte allein beweist keinen nutzbaren Audiopfad.

## Untersuchungsfolge und Reproduzierbarkeit

Die interne Untersuchung trennt vier Nachweisarten:

1. **Inventar:** ACPI-Ressourcen, SoundWire-Topologie, ALSA-Karten und PCM-Endpunkte sowie Treiberbindungen erfassen. Kernelkonfiguration und tatsächlichen Laufzeitstand getrennt protokollieren.
2. **Quellvertrag:** Den tatsächlichen Controller-, AFE-, Codec- und Firmware-Ladepfad verfolgen. Treiberquellen, Firmwareeingänge und Prüfer mit Manifesten an feste Inhalte binden. Rückgabewerte, Veröffentlichungszeitpunkte, IRQs, PM und Fehlerpfade mitprüfen.
3. **Offline-Ausführung und Build:** Extrahierte echte Produktionsfunktionskörper mit klar markierten API-Ersatzstellen ausführen; Fehler injizieren und absichtlich geschwächte Varianten zurückweisen. Anschließend echte ARM64-Module, vollständige Modulversionsangaben, Exportabhängigkeiten und den gemeinsamen Modulbestand prüfen. Ein erfolgreicher Build oder `depmod` ist kein Hardwaretest; ohne `CONFIG_MODVERSIONS` besteht keine zusätzliche Import-CRC-Absicherung.
4. **Abgegrenzter Hardwareversuch:** Nur einen unabhängig geprüften, unveränderlichen Kandidaten auf einem frischen Teststart verwenden. Beobachterbereitschaft vor dem Laden nachweisen, Versuche einzeln begrenzen, tatsächliche Bindungen und Ereigniszeiten lesen und die abgeschlossene Evidenz unabhängig prüfen. Bei Abbruch keine Wiederholung, keinen Reset und kein erzwungenes Entladen als vermeintliche Fehlerbehebung anschließen.

Für eine Wiederholung müssen Quellstand, Konfiguration, Eingangsmanifeste, Testgrenzen und Akzeptanzregeln **vorher** identisch feststehen. Ein veränderter Kandidat ist ein neuer Versuch, keine Fortsetzung eines bereits abgebrochenen Laufs.

### Erhaltene Abbrüche und Korrekturen

- Ein früherer CS42L43-Firmwareversuch brach wegen einer falschen erwarteten Revisionsdarstellung ab. Rohfeld und vom Produktionscode dekodierter Wert waren nicht dieselbe Zahlendarstellung. Die spätere Korrektur macht den ursprünglichen Abbruch nicht rückwirkend erfolgreich.
- Ein früherer kombinierter Versuch verletzte seine damalige strikte Null-IRQ-Regel. Der Abbruch bleibt gültig. Erst ein neuer instrumentierter Kandidat erhielt eine vorab geprüfte, begrenzte Initialisierungsregel; kein laufender alter Versuch wurde gelockert.
- Ein vorgeschalteter Offline-Policy-Parser musste korrigiert werden. Sandbox-Tests und ein funktionierender Parser sind Vorbereitung, nicht Ersatz für den späteren echten Hardwarelauf.

Historische Fehlerberichte und unveränderte Artefaktversiegelungen gehören zur Nachweiskette. Sie dürfen nicht durch einen späteren PASS überschrieben werden.

## Tatsächlich akzeptierter Hardwareumfang

Der abschließend unabhängig geprüfte Lauf mit Testkernel `7.2.8-yoga-audio-v2` erreichte ausschließlich **No-Stream-Kartenregistrierung**:

- Sieben geordnete private Modul-Ladeversuche kehrten erfolgreich zurück.
- Die reale Karte `Yoga-real-nostream-v1` wurde mit einem Backend instanziiert: `NVDA9100:00 / SDW1_Playback3` → `cs42l43-codec / cs42l43-dp5`, Plattform `NVDA9022:00`.
- Die tatsächlich aufgelöste Allokation war `[2,5,7,8]`, mit **`no_pcm=true`**. Der vorhandene HDMI-PCM-Bestand blieb unverändert; es entstand kein interner Benutzer-PCM.
- Alle drei SoundWire-Slaves waren `Attached`. Beide Verstärker blieben **ungebunden**. Der Codec war gebunden; SPI- und Pinctrl-Untergeräte hatten keine Treiberbindung.
- Parent und Codec meldeten aktiven Runtime-PM-Zustand. Der PM-Nutzungszähler war nicht verfügbar und wurde nicht als bekannt ausgegeben.
- Ein Parent-IRQ sowie je ein HP-Shutdown- und Tip-PLUG-Ereignis lagen nach Kernel-Emissionszeit streng vor der Codec-Veröffentlichung. Andere verschachtelte Ereigniszähler blieben null. Das erfüllt die endliche Initialisierungsregel, erklärt aber weder die Herkunft gelatchter Statusbits noch einen physischen Steckvorgang.
- Nach der letzten Laderückkehr deckten 94 Stichproben gut 60 Sekunden ohne IRQ-, Topologie- oder Resetänderung ab. Der unabhängige Review bestätigte die versiegelten 39 Evidenzdateien.

**Nicht geprüft:** funktionales AFE, Streamstart, Routing, Verstärker-Firmwareaktivierung, Lautsprecherschutz, Kalibrierung, Lautstärke, hörbare Ausgabe, Audioaufnahme oder Suspend/Resume des Audiopfads. Auch der No-Stream-Aufbau enthält aktive Controller-/Codecinitialisierung und ist kein allgemein gefahrloser passiver Scan.

## Offline geklärt: Verstärkerdateien und Speaker-Set

Die gespeicherte Hardwareidentifikation beider CS35L56 lautet B0, ungesichert, ROM-Version 3.4.4, ungepatcht. Das ist **ältere Hardwareevidenz**, keine aktuelle erneute Abfrage.

Die Offline-Prüfung des vorgesehenen 3.13.4-Abbilds und der Koeffizienten umfasst 42 Algorithmen und 204 Blöcke aus vier Koeffizientendateien. Algorithmen, Versionen und Schreibgrenzen wurden gegen den tatsächlichen Ladevertrag geprüft. Die reale Dateiauswahl wurde mit kompilierten Produktionsfunktionskörpern, aber ersetzten Datei-/DSP-Schnittstellen getestet.

Die spätere statische Auswertung des gespeicherten Windows-Pakets schließt die zuvor offene Standardzuordnung: `SdwSpeaker`-Nutzbyte `d0` ergibt bei den Paket-Standardselektoren **SS0**; die relevanten INFs überschreiben diese Selektoren nicht. Das ist ein unabhängiger Decoderbefund, nicht bloß eine Übertragung von Linux `spkid0`. Ein historischer Windows-Laufzeitnachweis des endgültig geladenen Dateinamens fehlt weiterhin.

Der daraus abgeleitete Kandidat besteht aus einem gemeinsamen Abbild und zwei UID-spezifischen Koeffizienten:

- `cirrus/cs35l56-b0-dsp1-misc-17aa3805-spkid0.wmfw`
- `cirrus/cs35l56-b0-dsp1-misc-17aa3805-spkid0-l1u0.bin`
- `cirrus/cs35l56-b0-dsp1-misc-17aa3805-spkid0-l1u1.bin`

**Diese Dateien werden hier nicht mitgeliefert und sind keine Installationsfreigabe.** Geänderter Patch-/Sicherheitszustand verändert die Dateinamenlogik. Ein erfolgreicher normaler Ladeaufruf kann außerdem ohne vollständige Koeffizienten zurückkehren. Tatsächliche Dateiauswahl und beide Tunings müssen deshalb separat nachgewiesen werden. UID-/Dateinamen beweisen weder physische Links-/Rechtslage noch Schutz- und Kalibrierungswirksamkeit.

## Warum das funktionale AFE weiterhin gesperrt ist

Der unabhängige IRQ-Review reproduzierte Produktionskörpertests über 22 IRQ-Quellen und 71 Initialisierungsfehlerpositionen. Das verbessert die softwareseitige Begründung, zertifiziert aber weder nebenläufige IRQ-/PCM-Lebenszyklen noch echte Registerzugriffe.

Die anschließende Init-only-Prüfung identifiziert drei konkrete Hardware-/Ownership-Lücken:

1. **Gemeinsame SSPM-Takte und Versorgung:** Controller und AFE verwenden gleiche Firmwareaktionen. Daraus folgen keine garantierte Mehrfachbenutzbarkeit, Referenzzählung oder sichere zweite Deinitialisierung bei aktivem SoundWire.
2. **Geerbte DMA-Zustände:** IRQ-Maskierung und Quittierung stoppen oder leeren keine DMA. Gegenbeispiele mit den echten MEMIF-Deskriptoren erhalten gesetzte Enable-/Adresszustände über Erfolgs- und Fehlerpräfixe. Diese Zustände sind synthetische Zeugen, keine auf dem Gerät gemessene Altlast. Ein belegter Stop-/Drain-/Idle-/Resetvertrag fehlt.
3. **PM und Fehlerabwicklung:** Rückabwicklung kann selbst fehlschlagen und gemischte Domain-/Taktzustände zurücklassen. Der volle Probe-Pfad kann trotz bestimmter PM-Zustände den Datenpfad aktivieren und Komponenten veröffentlichen. Er ist daher keine sichere Init-only-Abkürzung.

Das daraus gebaute Verweigerungsartefakt ist **kein Treiberfortschritt für die Hardware**: Probe und PM verweigern ausdrücklich, funktionale Initialisierung ist nicht implementiert, `ready_to_load=false`. Es soll nicht installiert werden.

## Weitere Offline-Erkenntnis: DSP-Laden ohne funktionales AFE

Die anschließende Untersuchung `amp-muted-firmware-firstload-v1` trennt zwei APIs: Der ASoC-Dateiresolver in `wm_adsp` benötigt weiterhin einen echten Component-Kontext. Der darunterliegende Produktionspfad `cs_dsp_power_up()` kann dagegen echte Firmware- und Koeffizientenobjekte ohne Card oder AFE entgegennehmen. Ein künstlicher Component-Kontext ist dafür weder erforderlich noch eine zulässige Abkürzung.

Der unveränderte Produktions-DSP-Core wurde für ARM64 gebaut; extrahierte Produktionspfade und eine exakte Drei-Dateien-Bundleprüfung wurden offline ausgeführt. Das ist **kein fertiger Verstärkertreiber und kein freigegebener Firmware-Erstladekandidat**. Die neuen Artefakte wurden zusätzlich anhand ihrer vollständigen Delivery-Manifest-Einträge auf Integrität geprüft; eine unabhängige Wiederholung aller neuen Tests steht noch aus.

Der engste Blocker ist jetzt klarer: Ein hardwareseitiger Ausgangsschutz über Shutdown, Download, Reset, Wiederanbindung und Fehler hinweg ist nicht belegt. Die normale Register-/Cacheinitialisierung setzt den Firmware-User-Mute auf 0; einmaliges Stummschalten ist deshalb keine bewiesene Invariante. Produktionspfadtests zeigen außerdem ignorierte Schreibfehler und Erfolgszustände trotz bestimmter Status-/Resetfehler. Das sind injizierte Offline-Gegenbeispiele, keine beobachteten Fehlvorgänge auf dem Yoga. Sie beweisen insbesondere nicht, dass ohne PLAY-Befehl tatsächlich Ton ausgegeben würde.

Die technisch begründete Integrationsrichtung ist ein komponentenfreier Loader mit denselben gehaltenen, vollständig verifizierten Firmwareobjekten. Vor seiner Aktivierung fehlen weiterhin der belastbare Output-Inhibit-/Reset-Vertrag und die geprüfte PM-/Worker-/Fehlerlebensdauer. Der AFE-Blocker wird dadurch nicht aufgehoben.

## Nächste Akzeptanzkriterien

- **Verstärker als getrennte Vorstufe:** Erst eine unabhängig geprüfte echte Firmware-/Tuning-Ladegrenze ohne funktionales AFE und ohne normale Machine-/PCM-Freigabe entwickeln. Mute und physisch ausgeschaltete Ausgänge müssen über Download, Reset, Wiederanbindung, Kalibrierung und Fehlerausgänge erhalten bleiben; fehlender PCM allein beweist das nicht. Diese Vorstufe ist noch kein freigegebener Hardwarekandidat.
- **Vor einem solchen Hardwaretest:** Aktuelle Silizium-/Sicherheits-/Firmwarezustände, sämtliche Resolverquellen und beide exakten Koeffizienten prüfen. Tatsächlich gewählte Dateien, Firmwarezustand beider Verstärker, Tuning-/Kanalidentitäten, stabile SoundWire-Topologie und unveränderte PCM-Grenzen unabhängig beobachten.
- **AFE:** Gemeinsamen Firmware-Ownervertrag und sicheren DMA-Stillstand belegen; PM-/Unwind-/Veröffentlichungsgrenzen einschließlich Fehlern und Lebensdauer prüfen. Zeitablauf in Userspace ist kein Stillstandsnachweis.
- **Vor jedem Unmute:** Schutz, Kalibrierung und reale Kanal-/Routenzuordnung nachweisen. Erst danach separat PCM, Machine-/DAPM-Routen, Userspace und kontrollierte hörbare Ausgabe abnehmen.

## Herkunft und Veröffentlichungsgrenze

Ausgewertet wurden insbesondere folgende **logischen internen Artefaktnamen**, nicht im Repository enthalten:

- `audio-next-kernel/combined-parser-freshboot-run-20261110/RESULT.md` und `PARENT-REVIEW.md`
- `audio-next-kernel/combined-guarded-v2-parent-review/FINDINGS.md`
- `audio-next-kernel/controlled-cs42-firmware-v2/PARENT-FIRMWARE-RESULT.md`
- `audio-next-kernel/afe-functional-irq-parent-review-v1/PARENT-REVIEW.md`
- `audio-next-kernel/afe-init-only-admission-v1/FINDINGS.md` und `HANDOFF.md`
- `audio-next-kernel/amp-firmware-selection/README.md`
- `audio-next-kernel/amp-speaker-set-resolution/README.md`
- `audio-next-kernel/amp-muted-firmware-firstload-v1/FINDINGS.md` und `HANDOFF.md` (neuer Abschluss, Integrität geprüft; vollständige unabhängige Testwiederholung noch offen)

Das sind interne Nachweise mit Quell-/Eingangspins und Reviews. **Die vollständige Beweiskette ist aus diesem öffentlichen Repository noch nicht unabhängig reproduzierbar.** Diese Seite enthält weder Rohprotokolle noch Patches, Module oder Firmware. Sie beschreibt die reproduzierbare Untersuchungsmethode und die belegte Ergebnisgrenze, nicht ein öffentlich verfügbares Testpaket.
