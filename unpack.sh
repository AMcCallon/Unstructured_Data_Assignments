
#!/usr/bin/env bash
CURR_DIR=/home/vagrant/work/week6/cwl-data/data/structured
NEW_DIR=/home/vagrant/work/week7/cwl-data/data/structured

#For loop to untar all tarballs in current directory
for TARFILE in structured-2018*.tar.gz;
do
	cd "$CURR_DIR"
	mv "$TARFILE" "$NEW_DIR"
	cd "$NEW_DIR"
	tar xzvf  "$TARFILE"
	rm "$TARFILE"
	cd "$CURR_DIR"

done
cd "$NEW_DIR"
#rm structured-2018*.tar.gz;
echo All done
