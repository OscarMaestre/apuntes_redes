NOMBRE_ARCHIVO=tabla_binario
NOMBRE_TXT=$(NOMBRE_ARCHIVO).txt
NOMBRE_PS=$(NOMBRE_ARCHIVO).ps
NOMBRE_PDF=$(NOMBRE_ARCHIVO).pdf

#Cuidado, enscript no soporta UTF-8, así que mejor evitar las tildes
TEXTO_CABECERA="                        Tabla de binarios y decimales"

all:
	echo "----Este script crea una tabla con los 256 primeros binarios----\n\n";
	./generador_tabla_binario.py > $(NOMBRE_TXT) ;
	enscript -p $(NOMBRE_PS) -b $(TEXTO_CABECERA) $(NOMBRE_TXT);
	ps2pdf $(NOMBRE_PS) $(NOMBRE_PDF);
	rm $(NOMBRE_PS) 