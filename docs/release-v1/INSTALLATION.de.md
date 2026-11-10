# Installation: experimenteller Kernel public-v1

## Status und Geltungsbereich

Für das Lenovo Yoga Pro 9 15N1X11, Modellfamilie 83SR, mit bestehendem Fedora ARM64 und funktionierendem Wiederherstellungspfad. Dies ist **kein Erstinstallationsmedium und kein bereits bootgetestetes Komplettpaket**.

`7.2.8-yoga-usb4-public-v1` wurde gebaut und statisch geprüft, aber nicht installiert, gestartet oder auf Hardware abgenommen. Frühere erfolgreiche Starts, NVIDIA-/KDE- und USB4-Beobachtungen gelten für frühere Projektstände, nicht automatisch für diese neu gebauten Bytes. Secure Boot, Signaturen und Vertrauen der Module sind **nicht validiert**. Interner Ton, Kamera, Suspend/Resume und Langzeitstabilität sind nicht als gelöst zugesagt.

**Installationsfreigabe derzeit: GESPERRT.** Die Kernel-/Moduldateien sind konkret vorhanden; eine geprüfte öffentliche Grafik-Startintegration fehlt. Die genaue Lücke steht unten und in der [technischen Anleitung](INSTALLATION-TECHNIK.de.md). Nicht durch manuelles Laden oder Kopieren privater Dienste umgehen.

## Vorbereitungen ohne Systemänderung

1. Modell und ARM64, installierte Fedora-Version, Bootloader, separates `/boot` und EFI-Systempartition feststellen. Dieses Paket ersetzt weder shim/GRUB noch Fedora-Basispakete.
2. Einen tatsächlich funktionierenden Kernel samt Modulen, Initramfs, vollständigem BLS-Eintrag und funktionierender Passphrase-Entsperrung behalten. Zusätzlich den aktuell laufenden Diagnosekernel schützen. Laufender Kernel, Menübezeichnung und gespeicherter Standard sind drei getrennte Angaben.
3. Den Bootmenüzugang vorab kennen und erproben. Netzteil, lokale Tastatur/Anzeige, eigenes Rettungsmedium und eine private Sicherung der Bootdateien bereithalten. SSH allein genügt nicht bei fehlender Entsperrung oder Anzeige.
4. Eigene LUKS-Passphrase lokal verfügbar halten. Keine Passphrase, Schlüsseldatei, persönliche Initramfs oder vollständige Bootkommandozeile veröffentlichen. Weder bestehende Passphrase-Slots noch TPM-Einschreibungen verändern. TPM-Entsperrung ist keine Voraussetzung dieses Pakets.
5. Quellen, Lizenzen, Inhaltsmanifest und Prüfsummen aus demselben freigegebenen Release beschaffen. Archive zunächst ausschließlich in ein neues leeres Arbeitsverzeichnis außerhalb von `/boot` entpacken; keine Archivextraktion nach `/`. Vorher absolute Pfade, `..`, Links und Spezialdateien zurückweisen. Prüfsummen allein authentifizieren die Downloadquelle nicht.
6. Keine Dateien verschiedener Kernelreleases mischen, auch wenn Namen ähnlich sind. NVIDIA-Kernelmodule, ARM64-Userspace und GSP-Firmware benötigen exakt `615.78.08`; ein Distributionspaket mit anderer Version ist kein Ersatz.

## Was noch separat benötigt wird

Nicht mitgeliefert und nicht durch die offenen Kernelmodule ersetzt:

- rechtmäßig bezogene passende NVIDIA-GSP-Firmware und proprietäre ARM64-Bibliotheken einschließlich `libnvidia-rmapi-tegra`, korrekter SONAME-Verknüpfungen und nativer Abhängigkeiten;
- eine überprüfte Integration in Fedora libglvnd, EGL-Vendor-/GBM-/Wayland-Provider und den dynamischen Loader; nur `LD_LIBRARY_PATH` zu setzen ist für capability-behaftetes KWin kein ausreichender Nachweis;
- ein auf **public-v1** begrenzter, fail-closed Startcontroller samt SELinux-Kontexten und Boot-Opt-in, der Ressourcen-/IOMMU-Prüfung, residenten GPU-Metadatenhelfer, unabhängige vollständige PFN-Nachprüfung und NVIDIA-Ladereihenfolge sicher verbindet. Der bisherige interne Pfad nutzt `nv_pfn_probe.ko`; dieses Prüfmodul und der öffentliche Controller sind in den untersuchten Binärarchiven nicht enthalten;
- eine auf diesem Fedora lokal erzeugte und inhaltlich geprüfte Initramfs sowie ein neuer, auf die eigene Installation zugeschnittener BLS-Eintrag. Es wird keine private Initramfs verteilt.

Eine vorhandene private Installation dieser Bestandteile wird nicht stillschweigend vorausgesetzt. Das alte Grafikarchiv enthält einen durch die Korrektur **überholten Helfer**. Es ist kein allein installierbares Grafikpaket; Einzelheiten und exakte Pfade siehe Technik.

## Additiver manueller Ablauf nach Aufhebung der Sperre

Die folgenden Schritte sind eine **Vorlage für spätere manuelle Freigabe**, kein hier ausgeführter oder für public-v1 getesteter Installer. Vor privilegierten Änderungen alle Punkte der [Abnahmecheckliste](RELEASE-ABNAHME.de.md) abschließen.

1. **Bestand privat sichern:** alle behaltenen Images, Initramfs, Modulbäume, BLS-Einträge, EFI-Dateien, GRUB-Zustand und Parameterquellen mit Dateisatz und Hashes erfassen; die Sicherung selbst prüfen. Den ursprünglichen Booteintrag und gespeicherten Standard unverändert lassen; ausstehende einmalige Bootauswahl zuerst klären.
2. **Kandidat isoliert zusammensetzen:** die 145 Kernelmodule, genau vier passende NVIDIA-Module und ausschließlich den korrigierten Helfer in einem neuen Staging-Baum vereinen. Vollständigen Dateisatz, Release, AArch64, Vermagic und Symbolabhängigkeiten prüfen. Die Zahl 150 bezeichnet statische Modulprüfung, nicht 150 hardwaregetestete Komponenten.
3. **Initramfs nativ vorbereiten:** außerhalb von `/boot`, mit explizitem Kandidaten-Modulverzeichnis, Kandidaten-Image und Release. Storage, Verschlüsselung, Btrfs, Konsole und lokale Tastaturbelegung in der echten Ausgabe prüfen. NVIDIA und Helfer dürfen nicht vor den Sicherheitsprüfungen automatisch geladen werden. Keine Live-Media-Pfade oder privaten Entsperrschlüssel übernehmen.
4. **Platz und Schutzbestand nochmals prüfen:** tatsächliche Größen von Image, config, System.map und erzeugter Initramfs plus Reserve gegen freien Platz auf dem richtigen `/boot` prüfen. Bei Platzmangel abbrechen; keinen Rückfallkernel löschen.
5. **Nur neue Ziele anlegen:** den neuen releasebezogenen Modulbaum und die drei neuen Kerneldateien gemäß [Pfadtabelle](INSTALLATION-TECHNIK.de.md#2-zielzuordnung) anlegen; bereits vorhandene Kandidatenziele bedeuten Stopp statt Überschreiben. Initramfs erst nach Inhaltsprüfung an ihren neuen Zielpfad kopieren. Metadaten/SELinux-Kontexte prüfen, Hashes gegen Staging vergleichen.
6. **Zusätzlichen BLS-Eintrag anlegen:** bestehenden funktionierenden Eintrag als lokale Referenz verwenden, eigene Root-/Verschlüsselungsoptionen und deren Quotierung vollständig bewahren, nur Kandidatenreferenzen und ausdrücklich überprüfte Kandidatenpolicy ändern. Alter Eintrag, globale Parameterquellen und gespeicherter Standard bleiben unverändert. Keine automatische GRUB-Neugenerierung und kein `kernel-install add` als Abkürzung.
7. **Unabhängig zurücklesen:** installierte Zielpfade, vollständigen Dateisatz/Hashes, BLS-Referenzen einschließlich erlaubter Variablen, Signatur-/Bootpolicy und unveränderte alte Dateien sowie GRUB-Auswahl prüfen. Installation ist noch keine Bootfreigabe.
8. **Erster Start nur manuell:** erst nach eigener ausdrücklicher Freigabe am sichtbaren Bootmenü den neuen Eintrag ausschließlich für diesen Start wählen. Keine dauerhafte Standardumschaltung, kein Neustartskript, keine automatische `next_entry`-Programmierung. Lokale Passphrase-Eingabe und [Rückfall](ROLLBACK.de.md) müssen möglich bleiben.

Nach dem Start Kernelrelease, tatsächliche Kommandozeile und verschlüsselte Root prüfen, danach Grafikbindung, sichtbare Ausgabe und Desktop getrennt abnehmen. Ein erreichbares System ist kein Nachweis fehlerfreier Grafik. Bei Problemen den erhaltenen Rückfalleintrag verwenden; keine Module gewaltsam entladen.
