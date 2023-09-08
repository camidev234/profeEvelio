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
        Schema::create('calif_estudiantes', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger("codigo_alumno");
            $table->unsignedBigInteger("codigo_ficha");
            $table->unsignedBigInteger("id_competencia");
            $table->string("nota_obtenida", 2);
            $table->string("periodo_cal", 12);
            $table->foreign("codigo_alumno")->references('id')->on("alumnos");
            $table->foreign("codigo_ficha")->references('id')->on("fichas_alumnos");
            $table->foreign("id_competencia")->references('id')->on("competencias");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('calif_estudiantes');
    }
};
