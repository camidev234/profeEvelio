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
        Schema::create('planes_estudiantes', function (Blueprint $table) {
            $table->id();
            $table->string("descrip_plan", 500);
            $table->unsignedBigInteger("duracion_dias");
            $table->unsignedBigInteger("id_funcionarioACargo");
            $table->foreign("id_funcionarioACargo")->references('id')->on("funcionarios");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('planes_estudiantes');
    }
};
