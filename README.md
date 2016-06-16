Descripción
===========

Cliente para la conversión de ficheros en formato DXF a GML. Ver [servidor](https://github.com/Ayuntamiento-Zaragoza/dxf2gml-catastro).


Requisitos
==========

* Python >= 2.7


Especificaciones de los ficheros DXF
====================================

1. En el nombre de la capa se establecerá la referencia catastral (14 dígitos) o la referencia local.
2. Las geometrías deben ser sólidas y estar cerradas (el primer y último punto del polígono deben ser el mismo).


Ejemplo de uso en Windows
=========================

```
python c:\python27\Scripts\dxf2gml-catastro --server=192.168.1.5:80 --code=25831 c:\parcelas
```


Ejemplo de uso en Linux
=======================
```
dxf2gml-catastro --server=192.168.1.5:80 --code=25831 /home/user/parcelas
```


