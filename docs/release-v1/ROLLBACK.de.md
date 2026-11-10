# Rückfall ohne Löschen oder Standardwechsel

[Installation](INSTALLATION.de.md) · [Technik](INSTALLATION-TECHNIK.de.md) · [Abnahme](RELEASE-ABNAHME.de.md)

## Vor dem Versuch

Rückfall ist ein **erhaltener Bootpfad**, kein späteres Reparaturskript. Folgendes muss bereits vor dem ersten Kandidatenstart vorliegen:

- funktionierender alter Kernel, dazugehörige Module und Initramfs;
- unveränderter alter BLS-Eintrag mit vollständigen lokalen Optionen und korrekt aufgelösten Dateipfaden;
- unveränderter gespeicherter Bootstandard, keine unerwartete einmalige Auswahl;
- erreichbares Bootmenü und ein eigener bekannter Weg, es beim Start anzuzeigen;
- lokal verfügbare ursprüngliche LUKS-Passphrase und unveränderte Passphrase-Schlüsselplätze;
- geprüftes Rettungsmedium sowie eine private, inhaltlich geprüfte Sicherung von Bootdateien und Bootkonfiguration. Eine Sicherung auf demselben Datenträger ist kein Schutz vor dessen Ausfall.

Die im Projekt erhaltene Grafik-Menübezeichnung `7.2.8-yoga-nvidia` referenziert tatsächlich `7.2.8-yoga-usb4-v2`. Eine Menübezeichnung ist kein `uname -r`. Der zuletzt im Projekt bestätigte laufende Diagnosezweig war audio-v2; das ist keine aktuelle Live-Abfrage und kein Bootnachweis für public-v1. Alle vorhandenen akzeptierten und laufenden Pfade schützen, nicht nur einen aus dem Namen vermuteten Rückfall.

## Normaler Rückfall nach einem Test

1. Keine funktionierende Sitzung für einen ungeprüften Treiberwechsel beenden. Bei erforderlicher Wiederherstellung einen kontrollierten Neustart separat entscheiden; dieses Dokument startet ihn nicht automatisch.
2. Im vorhandenen sichtbaren Bootmenü **den vorab identifizierten alten Eintrag nur für diesen Start manuell auswählen**. Keinen gespeicherten Standard ändern. Der erste Kandidatentest wird ebenfalls nur so ausgewählt; diese Anleitung setzt kein `next_entry`.
3. Verschlüsseltes System bei Bedarf lokal mit der ursprünglichen Passphrase entsperren. Kein `headless`-Zwang, keine Löschung von Passphrase-Slots und keine neue TPM-Einschreibung für den Rückfall.
4. Nach Start prüfen: tatsächlicher alter Kernel, korrekte verschlüsselte Root, alte BLS-Referenzen und alter gespeicherter Standard. Grafik, Anmeldung und lokale Erreichbarkeit separat bestätigen. Bloße Netzwerkerreichbarkeit ersetzt keine sichtbare Anzeige.
5. Den Kandidaten bis zur Ursachenklärung nicht erneut auswählen. Seine Dateien bleiben liegen; Rückfall erfordert weder Löschen noch eine erneute Installation des alten Kernels.

## Wenn Menü, Konsole oder Entsperrung fehlen

Nicht den Installer erneut starten, keine Partition formatieren und keine vorhandene Initramfs blind regenerieren. Das eigene geprüfte Rettungsmedium verwenden und die bestehende Installation zunächst nur lesen. Bei ext4-`/boot` kann `ro` allein Journalwiederholung zulassen; eine fachkundige Prüfung berücksichtigt `ro,noload`. Geräte und Mounts müssen am eigenen System eindeutig bestimmt sein; deshalb hier keine fremden Partitionsnamen oder universelle Mount-/Entsperrbefehle.

Vor einer gezielten Reparatur den alten und neuen BLS-Eintrag und deren tatsächliche Image-/Initramfs-Dateien prüfen, private Sicherungen gegen Hashes vergleichen und effektive Bootauswahl feststellen. Ein schwarzer Bildschirm oder fehlendes SSH beweist weder Kernelpanic noch eine bestimmte defekte Komponente. Vollständige Logs, UUIDs, Schlüssel und Initramfs nicht in öffentliche Issues hochladen.

## Was ausdrücklich kein Rückfall ist

- Kein `kernel-install remove`, keine Modulbaum-/BLS-/Image-Löschung und kein Aufräumen zur Platzgewinnung.
- Kein `grub2-set-default`, keine GRUB-Neugenerierung, kein EFI-Loader-Austausch.
- Kein erzwungenes Entladen des residenten `yoga_gpu_gap`-Helfers. Seine Metadatenregistrierung lebt bis zum Neustart; ein manueller Unload-Versuch kann diesen Sicherheitsvertrag brechen.
- Kein Kopieren alter Module unter das neue Release und kein Ignorieren eines Releaseguards.
- Kein automatisches Wiederholen des Kandidatenboots.

Falls eine spätere getrennt geprüfte Installation gemeinsame Grafikdienste oder Loaderkonfiguration ändert, muss sie **vorher** einen eigenen, konkret geprüften Rücknahmevertrag mitliefern. Die gegenwärtige Installationssperre besteht gerade auch deshalb: Das Kernel-/Modularchiv allein liefert diesen Vertrag nicht. Additive Kerneldateien machen unkontrollierte globale Grafikänderungen nicht automatisch rückfallfähig.
