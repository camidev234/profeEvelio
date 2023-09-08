<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\tipos_alumnos;
class Tipos_alumnosTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $tipo_uno = new tipos_alumnos();
        $tipo_uno->desc_tipo="este es el tipo de alumno uno";
        $tipo_uno->save();
    }
}
