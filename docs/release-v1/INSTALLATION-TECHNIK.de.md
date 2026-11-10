# Technische Installation: Layout, Bootintegration und Grenzen

[Allgemeine Anleitung](INSTALLATION.de.md) · [Rückfall](ROLLBACK.de.md) · [Abnahme](RELEASE-ABNAHME.de.md)

## 1. Tatsächlich inspizierter Paketstand

Diese Pfade wurden mit den tatsächlich zusammengestellten Kandidatenarchiven abgeglichen. Die Archivhashes und der vollständige Satz von 150 Modulen wurden unabhängig geprüft. Lokale Zusammenstellung ist keine Veröffentlichung und kein Installationstest.

Konstanten in den folgenden Tabellen:

- `R` = `7.2.8-yoga-usb4-public-v1` (vollständiges kompiliertes Release).
- `K/` = Archivwurzel `7.2.8-yoga-usb4-public-v1/` im Kernelarchiv `7.2.8-yoga-usb4-public-v1-kernel.tar.gz`.
- `G/` = Archivwurzel `7.2.8-yoga-usb4-public-v1-graphics/` im korrigierten Grafikarchiv `7.2.8-yoga-usb4-public-v1-graphics-corrected-v1.tar.gz`.
- Das separate frühere Korrekturarchiv ist für diese Zusammenstellung nicht zusätzlich einzuspielen; der korrigierte Helfer ist bereits in `G/` enthalten.

Die genannten Dateien sind lokal vorbereitete Kandidaten, keine Aussage, dass sie schon öffentlich angeboten werden. Quellen-/Lizenzfreigabe und Installation sind unabhängige Gates.

### Kernel und Metadaten

| Exakter relativer Archivpfad (mit obiger Wurzel) | Bedeutung |
|---|---|
| `K/Image` | ARM64-Kernelimage; kein RPM und keine Initramfs |
| `K/config` | tatsächlich verwendete Kernelkonfiguration |
| `K/System.map` | Symbolkarte für diesen Build |
| `K/Module.symvers` | Build-/Linkage-Nachweis für externe Module; kein Bootimage |
| `K/lib/modules/7.2.8-yoga-usb4-public-v1/kernel/` | 145 `.ko` aus dem Kernelbuild |
| `K/lib/modules/7.2.8-yoga-usb4-public-v1/modules.order` | Reihenfolge-/Inventarmetadaten |
| `K/lib/modules/7.2.8-yoga-usb4-public-v1/modules.builtin` | eingebaute Module |
| `K/lib/modules/7.2.8-yoga-usb4-public-v1/modules.builtin.modinfo` | Metadaten der eingebauten Module |
| `K/SHA256SUMS`, `K/manifest.json` | interne Integritäts-/Inhaltsnachweise |

### Korrigiertes Grafikpaket

Die vier unveränderten NVIDIA-Dateien liegen jeweils unter `G/lib/modules/7.2.8-yoga-usb4-public-v1/extra/`:

```text
nvidia.ko
nvidia-modeset.ko
nvidia-drm.ko
nvidia-uvm.ko
```

Der korrigierte Helfer liegt bereits unter `G/lib/modules/7.2.8-yoga-usb4-public-v1/extra/yoga_gpu_gap.ko`. Der vollständige Moduldateisatz wurde gegen den korrigierten kombinierten Stand geprüft. **Nicht verwenden:** das frühere Grafikarchiv mit `graphics-INTERNAL-DRAFT` im Namen; es enthält den überholten Helfer mit falschem Laufzeit-Guard. Kein zusätzliches Korrekturoverlay und keine Vermischung verschiedener Releases.

Korrigierter Helfer SHA256:

```text
ef8991a07b7ae0126e973acf5d8a9d28d8e68f78e3a51558539989b110a244c9
```

Die Korrektur ändert nur den exakten Releasevergleich, nicht die Modell-, Ressourcen-, Konfigurations- und Sicherheitsgrenzen. 13 Offline-Guardtests und die statische Prüfung aller 150 Module sind belegt; Ressourcenregistrierung, Laden, Grafikfunktion und Boot des neuen Builds sind damit **nicht** getestet. Vollständige Vermagic: `7.2.8-yoga-usb4-public-v1 SMP preempt mod_unload aarch64`.

## 2. Zielzuordnung

**Nur nach geschlossenem Installationsgate; hier nicht ausgeführt.** Neue Ziele müssen noch nicht existieren. Bestehende Releases und deren Dateiinhalte dürfen nicht ersetzt werden.

| Kandidatenquelle | Neu anzulegendes Fedora-Ziel |
|---|---|
| `K/Image` | `/boot/vmlinuz-7.2.8-yoga-usb4-public-v1` |
| `K/config` | `/boot/config-7.2.8-yoga-usb4-public-v1` |
| `K/System.map` | `/boot/System.map-7.2.8-yoga-usb4-public-v1` |
| Inhalt von `K/lib/modules/7.2.8-yoga-usb4-public-v1/` | `/usr/lib/modules/7.2.8-yoga-usb4-public-v1/` |
| die vier obigen NVIDIA-Dateien | jeweils `/usr/lib/modules/7.2.8-yoga-usb4-public-v1/extra/<Dateiname>` |
| `G/lib/modules/7.2.8-yoga-usb4-public-v1/extra/yoga_gpu_gap.ko` | `/usr/lib/modules/7.2.8-yoga-usb4-public-v1/extra/yoga_gpu_gap.ko` |
| lokal erzeugte, geprüfte Kandidaten-Initramfs | `/boot/initramfs-7.2.8-yoga-usb4-public-v1.img` |
| neuer lokaler BLS-Eintrag | eigene neue `.conf` unter `/boot/loader/entries/` |

Fedora verwendet den zusammengeführten `/usr`-Modulbaum. Das Archiv enthält `lib/modules`, nicht einen fertigen `/usr`-Installer: gezielt den releasebezogenen Inhalt übertragen, **nicht** den Archivwurzelordner unter `/usr/lib/modules` verschachteln und nicht unbesehen nach `/` entpacken. `/lib`-Auflösung auf dem konkreten System prüfen. Keine `build`-/`source`-Links in private Buildverzeichnisse übernehmen.

`Module.symvers` außerhalb des Bootpfades für Nachbau/Prüfung behalten. Es wird nicht als Kernel oder Initramfs installiert und ersetzt kein passendes Entwicklungs-/Buildpaket.

Die Metadaten `modules.order`, `modules.builtin` und `modules.builtin.modinfo` beim Staging erhalten. Die vorhandenen `modules.dep*` aus dem reinen Kernelpaket belegen keine Abhängigkeiten des zusammengesetzten Grafikpakets. Nach der endgültigen Zusammenstellung mit der passenden `System.map` neu prüfen. Der aufbewahrte kombinierte Nachweis meldet 150 AArch64-Module, vollständige Vermagic und `depmod -e -F System.map` ohne Warnungen. Er ist kein Laufzeittest und wurde hier nicht erneut ausgeführt.

## 3. Warum noch kein sicheres Grafik-Installationsrezept vorliegt

Ein Standardmodulbaum allein löst keine sichere Startreihenfolge. Der frühere interne Pfad führt zuerst Ressourcen-/IOMMU-Prüfungen und den residenten Metadatenhelfer aus, prüft danach den vollständigen GPU-Bereich unabhängig erneut und lädt erst dann die NVIDIA-Module mit passender Firmware. Der Helfer hat kein `module_exit`; seine registrierten Metadaten dürfen nicht durch Entladen invalidiert werden. Deshalb hier weder `insmod ... apply=1` noch ein Unload-/Reload-Rezept.

Die geprüften Kandidatenarchive enthalten **keinen** öffentlichen systemd-Controller, **keine** Boot-Opt-in-/Autoload-Konfiguration und **kein** `nv_pfn_probe.ko` für die unabhängige Nachprüfung. Das alte interne `yoga.nvidia=1` ist nur ein Schalter eines dort vorhandenen Controllers, kein eingebautes Aktivierungsmerkmal des Kernelarchivs. Seine Übernahme in eine neue Kommandozeile macht die fehlende Integration nicht verfügbar. Interne Quellen sind Evidenz, kein öffentlich freigegebener Installer.

Für eine Freigabe fehlen konkret: releasegebundener Controller samt Sicherheits-/Abbruchvertrag, öffentlich geprüfte vollständige PFN-Nachprüfung, Start-/Autoload- und Displaymanager-Reihenfolge, korrekte SELinux-Modultypen und lokal belegte Firmware-/Userspace-Integration. Der mitgelieferte `nouveau`-Treiber ist modular; konkurrierendes oder vorzeitiges Grafikautoload ist daher ausdrücklich zu behandeln. Keine globalen Blacklists oder alten Grafikdienste ohne Review ändern.

## 4. Initramfs: lokal und mit expliziten Eingaben

Keine vorhandene private Initramfs weitergeben. Die frühere native Vorbereitung nutzte `dracut` mit expliziten `--kmoddir`, `--kernel-image`, Konfigurations-/Konfigurationsverzeichnis, TMPDIR, Log- und Ausgabepfad sowie finalem Releaseargument. Sie lief mit schreibgeschütztem System und ausschließlich neuem Projektbereich als Schreibziel, ohne Netzwerk. Für den Loader-Cache brauchte diese Sandbox `CAP_SYS_CHROOT`; bloße Existenz der Ausgabe hätte einen ldconfig-Fehler nicht ausgeschlossen.

Die früher dokumentierten Optionen sind ein **Mechanismusnachweis eines anderen Kandidaten**, kein für public-v1 getesteter Befehl. Eine neue native Vorbereitung muss die auf dem installierten Fedora vorhandenen dracut-Module und Optionen prüfen und Folgendes gewährleisten:

- nicht das mit `uname -r` ermittelte laufende Release verwenden, sondern exakt `R`; Kandidatenkonfiguration im Staging berücksichtigen;
- Kandidatenmodulbaum und Image explizit verwenden, keine Installation nach `/usr/lib/modules` nur als Voraussetzung der Vorbereitung;
- NVMe/Root-LUKS berücksichtigen: `dm-crypt`, `essiv`, `nvme`, `nvme-core`; frühere native Vorbereitung ergänzte `vfat`, `fat`, `nls_iso8859-1`, `nls_utf8` und `crypt`/Btrfs/Console-Komponenten;
- tatsächliche `lsinitrd`-Dateirekorde für Module, cryptsetup samt Generator, Konsole/Passwortdienst, Tastaturbelegung, Btrfs und nativen ARM64-Loader prüfen; Btrfs ist hier eingebaut, NVMe und dm-crypt sind modular;
- `dmsquash-live`, `livenet` und `convertfs` beziehungsweise echte Live-Root-Payloads ausschließen; die Nennung hinter `--omit` in einer Argumentkopfzeile ist kein enthaltenes Modul;
- NVIDIA und Helfer nicht früh aus der Initramfs laden; erforderliche nichtöffentliche Firmware nicht ungeprüft einbetten. Bestehende Audio-/Kamera-Isolation nicht durch eine fremde Kandidatenliste ersetzen;
- eigenes TMPDIR auch für `lsinitrd` setzen: dieses Prüfwerkzeug kann temporäre Dateien erzeugen;
- reale Ausgabe, Log und Inhalt an denselben SHA256 binden, private Konfiguration/Schlüssel prüfen und actual-size-Platzprüfung vor jedem `/boot`-Schreibzugriff wiederholen.

Frühere additive Installation verwendete einen Sicherheitsaufschlag von 32 MiB. Das ist dokumentierter Mindestaufschlag, keine universelle Kapazitätsgarantie. Mehrbedarf des konkreten Systems zusätzlich bewerten.

## 5. BLS, kernel-install und dracut sind keine austauschbaren Installer

Historisch bestätigter Parameter**ausschnitt**:

```text
console=tty0 plymouth.enable=0 "acpi_osi=!Windows 2022" power_wrap_drv.usb4_release=0
```

Keine vollständige Kommandozeile. Eigene Root-/LUKS-/Btrfs-Optionen und bewusst gesetzte Isolationsparameter aus dem funktionierenden lokalen Eintrag vollständig erhalten. Der passende BLS-Kern lautet schematisch:

```text
title Fedora Yoga public-v1 TEST
version 7.2.8-yoga-usb4-public-v1
linux /vmlinuz-7.2.8-yoga-usb4-public-v1
initrd /initramfs-7.2.8-yoga-usb4-public-v1.img
```

Hier fehlt absichtlich `options`: es darf nicht aus allgemeinen Beispielen geraten werden. Die BLS-Pfade sind relativ zum Boot-Dateisystem, nicht zum entpackten Archiv. Dateinamen/Eintragskennungen lokal eindeutig wählen; keine fremde machine-id übernehmen. Vorhandene Variablen wie `$tuned_initrd` nur anhand des eigenen GRUB-Zustands gezielt expandieren; unbekannte Variablen bedeuten Stopp, eine erlaubte leere Expansion ist nicht automatisch ein fehlender Dateipfad.

Auf dem früher inspizierten Fedora konnten GRUB-Hooks BLS-Einträge trotz `kernel-install`-Layout `other` erzeugen. `UPDATEDEFAULT` und `GRUB_UPDATE_DEFAULT_KERNEL` sowie temporäre GRUB-Schlüssel sind zusammen relevant. Das vorhandene System vor Änderungen lesen; keine generische Entwarnung aus einem einzelnen Policywert ableiten.

Read-only-Inspektionsbeispiel **erst nach tatsächlichem Vorhandensein des neuen Images**, für diese public-v1-Installation nicht ausgeführt:

```sh
sudo kernel-install --no-pager inspect \
  7.2.8-yoga-usb4-public-v1 \
  /boot/vmlinuz-7.2.8-yoga-usb4-public-v1
```

Ein bloßes `kernel-install inspect` kann stattdessen unter `/usr/lib/modules/<release>/vmlinuz` suchen. `Initrds: (unset)` ohne Initrd-Argument widerlegt keine vorhandene BLS-Referenz. Nicht `kernel-install add` oder `grub2-mkconfig` als Diagnose ausführen: Hooks können Dateien, Optionen oder Bootauswahl ändern. Insbesondere kann GRUB-Neugenerierung aus altem `GRUB_CMDLINE_LINUX` die funktionierenden BLS-Optionen und `/etc/kernel/cmdline` überschreiben. Hier bleiben beide globalen Quellen und alle alten Einträge unangetastet.

## 6. Secure Boot und Signaturen

Die inspizierte Konfiguration enthält `CONFIG_EFI_STUB=y`, `CONFIG_MODULE_SIG=y`, aber weder `CONFIG_MODULE_SIG_FORCE` noch `CONFIG_MODULE_SIG_ALL`; `CONFIG_MODVERSIONS` ist ebenfalls aus. Das beweist weder einen vertrauenswürdig signierten Kernel noch akzeptierte externe Module. UEFI/shim-Vertrauenskette, Lockdown, Schlüsselerfassung und Modulannahme sind nicht validiert. Kein Deaktivieren von Secure Boot als stillschweigende Installationsvoraussetzung und keine private Signierschlüsselverteilung. Bei erforderlicher Signaturprüfung bleibt die Installation gesperrt, bis ein separat geprüfter Signier-/Trust-Prozess vorliegt.
