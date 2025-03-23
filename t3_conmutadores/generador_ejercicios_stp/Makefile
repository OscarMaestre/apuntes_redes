INPUT_EXT = .dot
OUTPUT_EXT = .png

all: $(patsubst %$(INPUT_EXT), %$(OUTPUT_EXT), $(wildcard *$(INPUT_EXT))) Ejercicios_stp.rst

Ejercicios_stp.rst: GeneradorEjercicios.py
	python3 GeneradorEjercicios.py

%.$(OUTPUT_EXT): %.$(INPUT_EXT)
	dot -Tpng $@ > $<

clean:
	rm *.dot; rm *.png