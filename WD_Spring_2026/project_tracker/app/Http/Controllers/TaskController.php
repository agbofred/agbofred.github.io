<?php
namespace App\Http\Controllers;

use App\Models\Task; // Note: No underscores, just Task!
use Illuminate\View\View;

class TaskController extends Controller
{
    public function index(): View
    {
        $tasks = Task::all(); 
        return view('tasks_index', compact('tasks'));
    }
}