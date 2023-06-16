# **Interprete Automatas**

## **Introducción:**
Existe un problema recurrente en las grandes ciudades a la hora de atender emergencias, ya seá Bomberos, Samu o Carabineros. El desarrollo de este interprete busca la reducción de dichos problemas facilitando el despacho de vehiculos bomberos según la emergencia.

## **Glosario:**
### Vehiculos:
En el mundo bomberil existen diversos vehiculos para diversas emergencias, con los que trabajaremos en este interprete son los siguientes:
- **B:** Bomba (Se encargan de llevar agua al llamado y apagar este mismo)
- **Q:** Porta-escalas (Llevan todo tipo de herramientas y escalas para destechar el siniestro)
- **R:** Rescate (Cuenta con herramientas de rescate, ya sea vehicular o peatonal)
- **M:** Escalas (Son escalas telescopicas montadas sobre carros capaces de llegar hasta los 55 metros)
- **H:** Hazmat (Se encargan de abastecer y alimentar a los carros bombas, así tambien de rellenar el oxigeno de los equipos ERA)

### Llamados:
La central de alarmas debe distinguir de que tipo de siniestro se trata, para ello se usan diversas claves, con las que se trabajaran ahora son las siguientes:
- **10-0-1:** Fuego estructural de menos de 4 pisos.
- **10-0-2:** Fuego estructural de 4 pisos o más.
- **10-4-1:** Choque de uno o más vehiculos con una persona atrapada.
- **10-4-2:** Choque de uno o más vehículos con dos o más personas atrapadas.

*Para mas claves click aquí:* [este link](https://wurtlitzer.com/bomberos/claves/metropolitana/santiago.php)

## **Funcionamiento:**
En el interprete usted deberá mencionar el tipo de llamado y luego decir si es "grave" o "tranqui". El output esperado será la cantidad y el tipo de máquinas que acuden al llamado.
**Ejemplo:** 
```
input: 10-0-1 tranqui
output: 2B 1Q
```
Esto quiere decir que al llamado acuden 2 carros bombas y 1 carro porta-escalas.
