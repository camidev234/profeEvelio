
<link rel="stylesheet" href="hd.css">
<?php

require('conexion.php');



$nombre_persona = $_POST['nombre'];
$primer_apellido_persona = $_POST['primer_apellido'];
$segundo_apellido_persona = $_POST['segundo_apellido'];
$edad_persona = $_POST['edad'];
$direccion_persona = $_POST['direccion'];

class Persona{

    private $nombre;
    private $primer_apellido;
    private $segundo_apellido;
    private $edad;
    private $direccion;

    public function __construct(string $nombre, string $primer_apellido, string $segundo_apellido, int $edad, string $direccion){
        $this->nombre = $nombre;
        $this->primer_apellido = $primer_apellido;
        $this->segundo_apellido = $segundo_apellido;
        $this->edad = $edad;
        $this->direccion = $direccion; 
    }

    public function getNombre():string {
        return $this->nombre;
    }

    public function getPrimerApellido():string{
        return $this->primer_apellido;
    }

    public function getSegundoApellido():string {
        return $this->segundo_apellido;
    }

    public function getEdad():int {
        return $this->edad;
    }

    public function getDireccion():string {
        return $this->direccion;
    }

    public static function crearPersona(){

        $arr_errores = [];
        global $conn, $nombre_persona, $primer_apellido_persona, $segundo_apellido_persona, $edad_persona, $direccion_persona;
        if (!$nombre_persona){
            $arr_errores[] = "El nombre de la persona esta vacio";
        }
        if (!$primer_apellido_persona){
            $arr_errores[] = "El primer apellido esta vacio";
        }
        if (!$segundo_apellido_persona){
            $arr_errores[] = "Segun apellido vacio";
        }
        if (!$edad_persona){
            $arr_errores[] = "Edad vacia";
        }
        if (!$direccion_persona){
            $arr_errores[] = "Direccion vacia";
        }

        if (empty($arr_errores)){
            $persona = new Persona("$nombre_persona", "$primer_apellido_persona", "$segundo_apellido_persona", "$edad_persona", "$direccion_persona");
            echo "Persona Creada Con exito";
            $sql = "INSERT INTO personas (nombre, primer_apellido, segundo_apellido, edad, direccion)
            VALUES ('$nombre_persona', '$primer_apellido_persona', '$segundo_apellido_persona', '$edad_persona', '$direccion_persona')";
            $query = mysqli_query($conn,$sql);
            return $persona;
        }else {
            foreach($arr_errores as $error){
                echo $error."</br>";
            }

            return false;
        }

    }

}

if(isset($_POST['enviar'])){
    $persona_nueva = Persona::crearPersona();
}

?>





