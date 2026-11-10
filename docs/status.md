# Hardwarestatus

[Übersicht](../README.md) · [Leitfaden](guide.md)

Dokumentierter Projektstand, **keine aktuelle Fernabfrage des Geräts**. Laufende Entwicklungsarbeiten ändern diese Tabelle erst nach Prüfung ihrer Ergebnisse.

| Bereich | Belegt | Offen / Einschränkung |
|---|---|---|
| Fedora-Start | Angepasster ARM64-Kernel startet auf dem Yoga; verschlüsseltes System erreicht Desktop | Keine Zusage für unveränderte Fedora-Installationsmedien oder andere Firmwarestände |
| Interne Eingabegeräte | Im angepassten Bootpfad nutzbar | Vollständige öffentliche Patch-/Buildzuordnung noch bereitzustellen |
| NVIDIA / KDE | Originalversion 615.78.08; reguläre KDE-Sitzung und NVIDIA-Rendering bestätigt | Bekannte Flip-/Abschaltprobleme aus isolierten Tests; Langzeit- und Resume-Abnahme offen |
| USB4 | Plattform-NHI und UCSI initialisiert, realer Link nachgewiesen | Keine vollständige Freigabe aller Betriebsarten, Ausgabewege oder Resume |
| Interner SoundWire-Bus | Reale Controller-/Codec-Topologie, isolierte Komponenten- und Cardinstanziierung bestätigt | Registrierung allein ist keine Audiofunktion |
| Lautsprecher | **Keine funktionierende Wiedergabe** | Funktionales AFE, DMA-/PM-Vertrag, Verstärker-Firmwaregrenze, Schutz/Kalibrierung und Routen offen |
| Mikrofone | Keine funktionale Aufnahmeabnahme | Ein-/Ausgaberouten und tatsächliche Aufnahme separat zu entwickeln |
| Kamera | Statische Sensor-/Startpfadrekonstruktion, GPIO-Output-Ownership und Offline-Vertragstests | **Keine native Aufnahme**; physischer Clock-/Power-/Reset-/CSI-/DMA-Vertrag unvollständig |
| Suspend / Resume | Nicht erfolgreich abgenommen | Nicht als stabil oder behoben betrachten |
| Öffentliche Downloads | Noch keine | Quell-, Lizenz-, Datenschutz- und Releaseprüfung erforderlich |

## Wie die Nachweise zu lesen sind

1. **Analyse:** aus tatsächlichen Quellen oder statischen Binärankern abgeleitet; keine Hardwaremessung.
2. **Offline-Test:** tatsächliche Produktionsfunktionen oder rekonstruierte Verträge geprüft; kein Ersatz für Kernel-/Hardwarekonkurrenz.
3. **Build:** ARM64-Kompilierung und Abhängigkeitsprüfung erfolgreich; noch keine Installations-/Ladefreigabe.
4. **Hardwaretest:** ein bestimmter Boot- und Testumfang wurde beobachtet; keine Generalisierung darüber hinaus.
5. **Funktion:** reale Bildausgabe, Wiedergabe oder Aufnahme nachgewiesen. Cardregistrierung oder ein erfolgreicher Modulladevorgang reichen dafür nicht.

## Öffentliche Nachprüfbarkeit

Die Texte sind aus vorhandenen Projektbefunden bereinigt abgeleitet. Die vollständigen internen Prüfprotokolle sind **nicht** Bestandteil dieses Repositorys. Eine externe Person kann die angegebenen Hardwaretests deshalb derzeit nicht anhand eines öffentlichen Evidenzpakets vollständig nachprüfen. Bereinigte Reproducer und releasebezogene Nachweise sollen schrittweise ergänzt werden; diese Lücke wird nicht als bereits gelöst dargestellt.
