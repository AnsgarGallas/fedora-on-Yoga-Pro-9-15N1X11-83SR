# Fedora auf dem Lenovo Yoga Pro 9 15N1X11 (83SR)

Hardwarebezogene Dokumentation zur Inbetriebnahme von Fedora ARM64 auf dem **Lenovo Yoga Pro 9 15N1X11, Modellfamilie 83SR**. Ziel ist ein nachvollziehbarer Weg vom sicheren Start bis zu funktionierender Grafik, internen Eingabegeräten, USB4, Audio und Kamera.

> **Entwicklungsstand, keine fertige Komplettlösung:** Ein angepasster Kernel ermöglicht den dokumentierten Start und NVIDIA-/KDE-Betrieb. Interne Lautsprecher und Kamera funktionieren noch nicht. Die Audio-Card im isolierten Test ist ausdrücklich **kein Wiedergabenachweis**. Aktuell enthält dieses Repository Dokumentation, keine installierbaren Releases.

## Voraussetzungen

- Genau dieses Yoga-Modell mit ARM64-Plattform; die Modellbezeichnung allein ist kein Nachweis für andere Gerätevarianten oder Firmwarestände.
- Fedora ARM64; die bisherigen Projektversuche beziehen sich auf Fedora 45 und angepasste Kernel der Reihe `7.2.8`.
- Ein überprüfter Rückfall-Bootpfad, Datensicherung und ein lokaler Zugriff auf das Bootmenü, bevor Kernel oder Bootparameter geändert werden.
- Für spätere Eigenbauten: die exakten Quellen, geordnete Patches, Konfiguration und passende ARM64-Werkzeuge. Dieses vollständige öffentliche Buildpaket steht noch aus.

## Zwei Leseebenen

### 1. Der Weg und die Schritte

Der [Leitfaden](docs/guide.md) erklärt Reihenfolge, Voraussetzungen, erreichte Ergebnisse und Abnahmekriterien. Die [Statusübersicht](docs/status.md) trennt Hardwaretests von Build- und Analyseergebnissen.

### 2. Die technischen Erkenntnisse

| Schritt | Vertiefung |
|---|---|
| Hardware abgrenzen, Kernel und Startpfad vorbereiten | [Boot und Kernel](docs/technical/boot-kernel.md) |
| NVIDIA-Grafik und regulärer KDE-Betrieb | [Grafik](docs/technical/graphics.md) |
| USB4, Plattformcontroller und Benachrichtigungen | [USB4](docs/technical/usb4.md) |
| Interner SoundWire-Audiopfad | [Audio](docs/technical/audio.md) |
| Native Kamerapipeline | [Kamera](docs/technical/camera.md) |

## Was veröffentlicht werden soll

Nach Prüfung: bereinigte Patches, Buildanleitungen und die zugehörigen Tests; anschließend geprüfte Linux-Treibermodule und ein zugehöriger Kernel mit vollständigem passenden Quellpaket, Lizenzen und Prüfsummen. **Extrahierte Windows-Treiber werden nicht veröffentlicht.** Firmware und proprietäre Bestandteile sind von Linux-Treibermodulen getrennt zu beurteilen.

- [Lizenz- und Releaseanforderungen](docs/distribution.md)
- [Konkrete Prüfung der vorhandenen Kernel und Module](docs/release-audit.md)
- [Datenschutz und Veröffentlichungsprüfung](docs/publication-policy.md)

Dieses Repository beschreibt ausschließlich die Yoga-Hardware. Persönliche Einrichtung, Konten, Netzwerke und Informationen über andere Geräte gehören nicht hierher. Eine Lizenz für die eigenen Dokumentationstexte ist noch festzulegen; vorhandene Fremdkomponenten behalten ihre jeweiligen Lizenzen.
