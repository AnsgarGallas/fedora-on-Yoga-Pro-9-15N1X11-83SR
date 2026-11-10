# Release-Abnahme: public-v1

[Installation](INSTALLATION.de.md) · [Technik](INSTALLATION-TECHNIK.de.md) · [Rückfall](ROLLBACK.de.md)

**Bedeutung:** `[x]` = hier anhand lokaler Evidenz beziehungsweise Archivinspektion belegt; `[ ]` = offen oder nicht in diesem Auftrag ausgeführt. Ein Haken bei statischer Evidenz ist keine Hardwareabnahme. Veröffentlichung, Installierbarkeit und Hardwarefunktion sind getrennte Entscheidungen.

## A. Byteidentität und statischer Stand

- [x] Vollständiges Kandidatenrelease `7.2.8-yoga-usb4-public-v1`; separate Identität gegenüber `7.2.8-yoga-usb4-v2` und audio-v2.
- [x] Endgültiger lokaler Kernelkandidat enthält Image, config, System.map, Module.symvers und 145 `.ko`; das korrigierte Grafikarchiv enthält vier NVIDIA-Module und genau den korrigierten Helfer.
- [x] Der Helfer-Guard wurde unabhängig erneut ausgeführt: Original scheitert, Korrektur besteht 13 Prüfungen. Die Assembly enthält exakt die 150 erwarteten AArch64-Module mit passender vollständiger Vermagic und identischen Hashes zum korrigierten kombinierten Stand. Der Assembly-depmod-Nachweis ist separat vorhanden; im unabhängigen Modulhashreview wurde depmod nicht erneut ausgeführt.
- [x] Endgültige Archivnamen, Wurzeln und Helferpfad mit der technischen Anleitung abgeglichen; alle neun Einträge der äußeren SHA256SUMS unabhängig bestätigt.
- [x] Keine zweite alte Helfer-Moduldatei und keine Vermischung von Kernelreleases in den beiden Binärarchiven.

## B. Veröffentlichungsfreigabe — getrennt von Installation

- [ ] Vollständige passende Kernel-, NVIDIA- und Helferquellen einschließlich tatsächlicher Änderungen, Konfiguration und Build-/Installationsunterlagen am gleichen Releaseort verfügbar; Dokumentationsrepo-ZIP allein reicht nicht.
- [x] Dateispezifische Lizenz-/Attributions-/Änderungshinweise und erforderliche vollständige Drittanbieter-Lizenztexte im abgegrenzten lokalen Sieben-Archiv-Kandidaten unabhängig geprüft.
- [ ] Tatsächliche öffentliche Quelldateien, Binärbytes, Dateinamen und Manifeste unabhängig auf private Metadaten geprüft; keine privaten Schlüssel, private Initramfs, persönlichen Bootarchive oder ungeklärte Firmware-/Userspace-Dateien.
- [ ] Nach Veröffentlichung alle öffentlichen Statusaussagen auf den tatsächlichen Download abgleichen; abgeschlossene lokale Quellen-/Hinweisprüfung, öffentliche Verfügbarkeit und weiterhin gesperrte native Installation unterscheiden. Keinen unbestätigten Boot-/Hardwareerfolg behaupten.
- [ ] Dokumente und genaue Releaseassets manuell geprüft. Lokale Vorbereitung ist weder Commit noch Push noch Releaseupload.

## C. Installationsbereitschaft — derzeit GESPERRT

- [ ] Öffentlicher releasegebundener Grafikcontroller mit Ressourcen-/IOMMU-Prüfung, residentem Helfer, unabhängiger vollständiger PFN-Nachprüfung und sicherer Ladereihenfolge vorhanden und geprüft. `nv_pfn_probe.ko` fehlt in den untersuchten Binärarchiven; allein der korrigierte Helfer ersetzt die Nachprüfung nicht.
- [ ] Boot-Opt-in, Verhinderung verfrühten/konkurrierenden Autoloads einschließlich nouveau und Initramfs, Displaymanager-/KWin-Reihenfolge, SELinux-Modultypen und Rücknahme gemeinsamer Grafikänderungen konkret geprüft. Keine ungeprüfte Wiederverwendung privater Dienste.
- [ ] Proprietäre ARM64-Bibliotheken, SONAME-Verknüpfungen, libglvnd-/EGL-/GBM-/Wayland-/Loader-Integration und passende GSP-Firmware für exakt NVIDIA `615.78.08` separat rechtmäßig beschafft und lokal verifiziert; nicht Teil des offenen Modularchivs.
- [ ] Secure-Boot-/shim-/Lockdown-Zustand und benötigte Image-/Modulsignaturen sowie Trust-Verfahren geprüft. **Derzeit nicht validiert**, kein stillschweigender Wechsel der Sicherheitskonfiguration.
- [ ] Konkretes Fedora, native dracut-Version/-Module und Boot-Hooks erfasst. Kandidaten-Initramfs außerhalb `/boot` erzeugt und echte Payload auf Storage, LUKS, Btrfs, Konsole, lokale Tastatur, Ausschlüsse und private Schlüssel geprüft; Logs ohne unaufgeklärte Fehler.
- [ ] Modell/Architektur, richtige System-/Bootmounts, ursprüngliche Passphrase, sichtbares Menü und Rettungsmedium lokal verifiziert; keine automatische Entsperrung vorausgesetzt.
- [ ] Schutzmanifest für alle behaltenen Images, Initramfs, Module, BLS, EFI, GRUB-Zustand und globale Parameterquellen privat gesichert und geprüft.
- [ ] Genügend Platz für **tatsächliche** neue Bootdateigrößen plus mindestens dokumentierten 32-MiB-Aufschlag und systemspezifische Reserve; keine Löschung als Nebenwirkung.
- [ ] Alle neuen Zielpfade frei; ausdrückliche Freigabe genau dieser additiven Installation liegt vor. Boot und Standardwechsel sind nicht eingeschlossen.

## D. Nach additiver Installation — noch nicht erfolgt

- [ ] Frisches unabhängiges Zurücklesen: alle neuen Zielhashes und vollständiger Moduldateisatz exakt gleich Staging; SELinux-Kontexte richtig.
- [ ] Neue BLS-Referenzen existieren, Variablen gezielt aufgelöst, lokale Root-/LUKS-/Btrfs-Optionen und Quotierung erhalten; Kandidatenpolicy überprüft.
- [ ] Alle alten Dateien/Einträge unverändert, gespeicherter Standard unverändert, keine unerwartete einmalige Auswahl. Kein globaler Parameterquellenwechsel, kein automatischer Neustart.
- [ ] Lokale manuelle Bootmenüauswahl und Passphrase-Rückfall erklärt; erster Start separat freigegeben.

## E. Erster Boot und Hardware — alles für public-v1 offen

- [ ] Manuelle einmalige Menüauswahl führte tatsächlich zum neuen Kernel; geänderter Boot und exakt `uname -r = 7.2.8-yoga-usb4-public-v1` bestätigt.
- [ ] Verschlüsselte Root, effektive Parameter, erhaltene Passphrase-Entsperrung und alter gespeicherter Standard bestätigt.
- [ ] Ressourcen-/IOMMU-Vertrag und unabhängige vollständige GPU-PFN-Nachprüfung bestanden, danach erwartete NVIDIA-PCI-/DRM-Bindung mit passenden Modulen/Firmware.
- [ ] Sichtbare Anzeige, reguläre Anmeldung, tatsächlich GPU-basiertes Rendering und KDE getrennt bestätigt; Kernel-/Dienstwarnungen einschließlich Shutdown-Befunden bewertet.
- [ ] USB4-Controller, UCSI, physischer Link, Carrier und gegebenenfalls Datentransfer getrennt geprüft; alter Erfolg nicht auf public-v1 übertragen.
- [ ] Manueller Rückfall in den erhaltenen alten Eintrag einschließlich Entsperrung nachweisbar.
- [ ] Interner Ton, Kamera, Suspend/Resume und Langzeitstabilität separat geprüft oder weiterhin ausdrücklich als nicht abgenommen bezeichnet. Build-/Guardtests ersetzen keine dieser Prüfungen.

**Freigaberegel:** Erst nach B kann ein experimentelles, wahrheitsgemäß begrenztes Binärrelease zur Veröffentlichung beurteilt werden. Erst nach C ist eine Installation freigabefähig, erst nach D ein separat genehmigter Bootversuch. E darf nicht durch ein pauschales „PASS“ aus A ersetzt werden. Keine dieser Stufen verlangt einen automatischen Standardwechsel.
