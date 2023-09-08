<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\tipos_alumnos;
/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\tipos_alumnos>
 */
class tipos_alumnosFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'desc_tipo'=>$this->faker->sentence()
        ];
    }
}
