SOURCE=generateFile.py
EXEC=g--
CONF_PATH=/etc/g--
INSTALL_PATH=/usr/local/bin

install: $(EXEC) $(CONF_PATH)

$(EXEC):
	cp $(SOURCE) $(INSTALL_PATH)/$(EXEC)
	chmod +x $(INSTALL_PATH)/$(EXEC)

$(CONF_PATH):
	if [ ! -d $(CONF_PATH) ]; then mkdir $(CONF_PATH); fi
	cp *Template $(CONF_PATH)

uninstall:
	rm -R $(CONF_PATH)
	rm $(INSTALL_PATH)/$(EXEC)
