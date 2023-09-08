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
        Schema::create('profesores_fichas', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger("id_profe_ficha");
            $table->unsignedBigInteger("codigo_ficha");
            $table->foreign("id_profe_ficha")->references('id')->on("profesores");
            $table->foreign("codigo_ficha")->references('id')->on("fichas_alumnos");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('profesores_fichas');
    }
};
