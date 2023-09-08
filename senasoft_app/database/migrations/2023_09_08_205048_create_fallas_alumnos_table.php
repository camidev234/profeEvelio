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
        Schema::create('fallas_alumnos', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger("codigo_alumno");
            $table->unsignedBigInteger("ficha_adscrita");
            $table->date("fecha_falla");
            $table->string("motivo", 255);
            $table->string("justificacion", 133);
            $table->foreign("codigo_alumno")->references('id')->on("alumnos");
            $table->foreign("ficha_adscrita")->references('id')->on("fichas_alumnos");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('fallas_alumnos');
    }
};
