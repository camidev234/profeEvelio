<?php

$numero_uno = intval($_POST['numUno']);
$numero_dos = intval($_POST['numDos']);

class Calculadora {



    private $num_uno;
    private $num_dos;


    public function __construct(int $num_uno, int $num_dos) {
        $this->num_uno = $num_uno;
        $this->num_dos = $num_dos;

    }

    private function comprobarCampos():bool {
        global $numero_uno, $numero_dos;
        $arr_errores = [];
        if(!$numero_uno){
            $arr_errores[] = "Falta el numero Uno";
        }
        if(!$numero_dos){
            $arr_errores[] = "Falta el numero dos"; 
        }

        

        if(empty($arr_errores)){
            return true;
        } else{
            return false;
        }
    }

    public function sumar(){
        $resultado = $this->comprobarCampos();


        if($resultado){
            echo $this->num_uno + $this->num_dos;
        } else{
            return "hubo error al momento de reaaalizar la operacion";
        } 
    }

    public function restar(){
        $resultado = $this->comprobarCampos();


        if($resultado){
            return $this->num_uno - $this->num_dos;
        } else{
            return "hubo error al momento de reaaalizar la operacion";
        } 

    }

    public function multiplicacion(){
        $resultado = $this->comprobarCampos();

        if($resultado){
            return $this->num_uno * $this->num_dos;
        } else{
            return "hubo error al momento de reaaalizar la operacion";
        } 
    }

    public function division(){
        $resultado = $this->comprobarCampos();

        if($resultado){
            return $this->num_uno / $this->num_dos;
        } else{
            return "hubo error al momento de reaaalizar la operacion";
        } 
    }
    public function ejecutarOperacion(){
        global $operacion;
        if (isset($_POST['operacion'])){
            $operacionSeleccionada = $_POST['operacion'];
       
        if($operacionSeleccionada === "suma"){
             echo $this->sumar();
        } else if ($operacionSeleccionada === "resta"){
            echo $this->restar();
        } else if ($operacionSeleccionada === "multiplicacion"){
            echo $this->multiplicacion();
        } else if ($operacionSeleccionada === "division"){
            echo $this->division();
        }
    } 
    }
}

$calcUno = new Calculadora($numero_uno, $numero_dos);
$calcUno->ejecutarOperacion();
// echo $calcUno->sumar();
// echo $calcUno->restar();


?>