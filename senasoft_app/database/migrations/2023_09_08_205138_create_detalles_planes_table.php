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
        Schema::create('detalles_planes', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger("id_plan");
            $table->unsignedBigInteger("id_alumno");
            $table->string("oservaciones", 700);
            $table->foreign("id_plan")->references('id')->on("planes_estudiantes");
            $table->foreign("id_alumno")->references('id')->on("alumnos");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('detalles_planes');
    }
};
