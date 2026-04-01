<?php

namespace App\Http\Controllers;

use App\Models\ProjectTracker; // Import the Model
use Illuminate\View\View;

class ProjectTrackerController extends Controller
{
    public function index(): View
    {
        // Get all projects from the database
        $projects = Project_trackers::all();

        // Pass them to a view called 'dashboard'
        return view('dashboard', compact('projects'));
    }
}