<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('alumnos', function (Blueprint $table) {
            $table->id();
            $table->string("nombre_alumno", 40);
            $table->string("apellidos_alumnos", 70);
            $table->string("direccion_alumno", 50);
            $table->string("telefono", 17);
            $table->unsignedBigInteger("ficha_alumno");
            $table->unsignedBigInteger("estado_alumno");
            $table->unsignedBigInteger("tipo_alumno");
            $table->foreign("tipo_alumno")->references('id')->on("tipos_alumnos");
            $table->foreign("ficha_alumno")->references('id')->on("fichas_alumnos");
            $table->foreign("estado_alumno")->references('id')->on("estados_alumnos");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('alumnos');
    }
};
