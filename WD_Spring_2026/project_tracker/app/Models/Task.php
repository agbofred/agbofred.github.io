<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    // This allows you to fill the 'name' and 'priority' columns automatically
    protected $fillable = ['name', 'priority'];
}
