<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Task;

class TaskSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
       $priorities = ['High', 'Medium', 'Low'];

        for ($i = 1; $i <= 10; $i++) {
            Task::create([
                'name' => "Sample Task Number " . $i,
                'priority' => $priorities[array_rand($priorities)],
            ]);
        }
    }
}
