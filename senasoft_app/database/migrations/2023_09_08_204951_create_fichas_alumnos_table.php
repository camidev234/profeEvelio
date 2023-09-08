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
        Schema::create('fichas_alumnos', function (Blueprint $table) {
            $table->id();
            $table->string("codigo_ficha", 10);
            $table->string("descripcion_grupo", 100);
            $table->unsignedBigInteger("codigo_programa");
            $table->date("fecha_inicio");
            $table->date("fecha_fin");
            $table->unsignedBigInteger("id_jornada");
            $table->foreign("codigo_programa")->references('id')->on("programas");
            $table->foreign("id_jornada")->references('id')->on("jornadas");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('fichas_alumnos');
    }
};
