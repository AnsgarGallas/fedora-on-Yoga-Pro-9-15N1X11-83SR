# Leitfaden: vom Start zur vollständigen Hardwareunterstützung

[Übersicht](../README.md) · [Status](status.md)

## Ziel und Grenzen

Fedora ARM64 soll auf dem Yoga Pro 9 15N1X11 (83SR) mit nachvollziehbar gebautem Kernel und überprüften Linux-Treibern laufen. Zur vollständigen Lösung gehören auch interne Lautsprecher, Mikrofone, Kamera und verlässliches Energiemanagement. Nicht alle diese Ziele sind erreicht.

Die folgenden Schritte dokumentieren den tatsächlich erarbeiteten Weg. **Sie sind noch keine vollständige Installationsanleitung:** Öffentlich fehlen derzeit insbesondere das exakte Quell-/Patchpaket, bereinigte Buildskripte und freigegebene Binärartefakte. Unvollständige experimentelle Schritte dürfen nicht als Aktivierungsanweisung verstanden werden.

## 1. Modell und Hardwarepfade feststellen

**Warum:** ARM64-Unterstützung allein sagt nichts über die verbauten Plattformcontroller aus.

- Modellfamilie 83SR und ARM64 prüfen.
- ACPI-Geräte, gebundene Linux-Treiber und Kernelkonfiguration vergleichen.
- Grafik, USB4, internen SoundWire-Pfad und Kamera getrennt erfassen.
- Bei fehlendem Gerät unterscheiden: fehlende Kerneloption, fehlender Treiber, gesperrte automatische Bindung oder fehlende funktionale Integration.

**Ergebnis:** Die projektrelevanten Plattform- und Codec-IDs sind zugeordnet; eine reine Paketinstallation genügt für Audio und Kamera nicht. [Technik](technical/boot-kernel.md)

## 2. Einen rückfallfähigen Kernel-/Bootpfad aufbauen

**Voraussetzung:** Wiederherstellbarer Bootpfad und Sicherung der vorhandenen Bootdateien.

- Angepassten Kernel separat bauen; vorhandenen funktionierenden Kernel nicht ersetzen.
- Kernel, Konfiguration, Module und Bootdateien mit Prüfsummen festhalten.
- Neue Booteinträge additiv und zunächst nur für einen Teststart anlegen.
- Sichtbare Konsole und Entsperrung des verschlüsselten Systems unabhängig vom Grafikstart prüfen.

**Ergebnis:** Start bis zum Fedora-Desktop wurde erreicht. Konsole und Plymouth mussten im untersuchten Bootpfad getrennt behandelt werden. Ein erfolgreicher Start ersetzt keine Suspend-/Resume-Abnahme. [Technik](technical/boot-kernel.md)

## 3. Grafik schichtweise aktivieren

- Speicher-/IOMMU-Voraussetzungen aus der tatsächlichen Yoga-Firmware ableiten.
- NVIDIA-Kernelmodule, Firmware und ARM64-Bibliotheken versionsgleich halten.
- Kernelbindung, Bildausgabe, Rendering und reguläre KDE-Sitzung getrennt prüfen.
- Abschalt-, Resume- und Langzeitverhalten separat bewerten.

**Ergebnis:** NVIDIA `615.78.08` und regulärer KDE-/OpenGL-ES-Betrieb sind im Projekt bestätigt. Ein modellspezifischer Speicher-Metadaten-Workaround ist Teil des untersuchten Pfads; dies ist keine generelle Empfehlung für andere Firmwarestände. [Technik](technical/graphics.md)

## 4. USB4-Plattformintegration ergänzen

- Tatsächliche Plattform-NHI-Geräte und deren Abhängigkeiten bestimmen.
- FF-A-/ACPI-Interruptabbildung und UCSI-Benachrichtigungen prüfen.
- Controller, Router, Type-C und tatsächlichen Link nicht miteinander verwechseln.

**Ergebnis:** Plattformcontroller, UCSI und USB4-Link wurden im Projekt nachgewiesen. Daraus folgt keine pauschale Abnahme aller USB4-Funktionen oder des Resume-Verhaltens. [Technik](technical/usb4.md)

## 5. Audio ohne unbelegte Lautsprecheraktivierung entwickeln

- Controller und Codec-Topologie erfassen, bevor Firmware oder Verstärker aktiviert werden.
- Firmwareidentität, Komponentenregistrierung, IRQ-Verhalten und PCM-Funktion getrennt prüfen.
- Gemeinsame Clock-/Power-Verantwortung, DMA-Stillstand sowie Verstärkerschutz und Kalibrierung klären.
- Erst anschließend funktionale Routen und eine kontrollierte Wiedergabe abnehmen.

**Ergebnis:** Eine reale, isolierte No-stream-Card wurde hardwaregetestet. Sie erlaubt keinen Benutzer-PCM-Stream. Es gibt weiterhin keinen Ton; ein gebauter IRQ-Fix ist keine Freigabe des funktionalen AFE. [Technik](technical/audio.md)

## 6. Kamera vom Hardwarevertrag bis zum Bild entwickeln

- Eigene Firmware-/Treiberinformationen statisch untersuchen, nicht ausführen oder weiterverteilen.
- Sensor, Takt, Power/Reset, CSI-/PHY-, DMA-/IOMMU- und Medienpfad separat rekonstruieren.
- Nur belegte Sequenzen in einen Linux-Port übernehmen.

**Ergebnis:** Teile des Sensor- und Mailboxvertrags sind rekonstruiert und offline getestet. Der physische Sensortakt und weitere Startvoraussetzungen sind offen; native Aufnahme ist nicht erreicht. [Technik](technical/camera.md)

## 7. Aus einer Entwicklung ein nutzbares Release machen

Ein Release benötigt den passenden Quellstand, alle Patches, Konfiguration, Build-/Installationsskripte, Lizenztexte, Prüfsummen und eine klare Abnahme-/Rückfallbeschreibung. Module müssen exakt zum vorgesehenen Kernel passen. Experimentelle Diagnosemodule werden nicht als fertige Lösung angeboten.

**Ergebnis:** Dokumentation vorbereitet; kein öffentliches Kernel-/Treiberrelease vorhanden. [Releaseprüfung](distribution.md)
