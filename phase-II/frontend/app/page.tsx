'use client';

import { useEffect, useState } from 'react';

// Define TypeScript interfaces matching the backend models
interface User {
  id: string;
  email: string;
  first_name: string | null;
  last_name: string | null;
  created_at: string;
  updated_at: string;
}

interface Task {
  id: string;
  title: string;
  description: string | null;
  is_completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

interface NewUser {
  email: string;
  first_name: string;
  last_name: string;
  password: string;
}

interface NewTask {
  title: string;
  description: string;
  user_id: string;
  is_completed: boolean;
}

interface EditUser {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
}

interface EditTask {
  id: string;
  title: string;
  description: string;
  user_id: string;
  is_completed: boolean;
}

export default function Home() {
  const [users, setUsers] = useState<User[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newUser, setNewUser] = useState<NewUser>({ email: '', first_name: '', last_name: '', password: '' });
  const [newTask, setNewTask] = useState<NewTask>({ title: '', description: '', user_id: '', is_completed: false });
  const [activeTab, setActiveTab] = useState<'users' | 'tasks'>('users');
  const [editingUserId, setEditingUserId] = useState<string | null>(null);
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);
  const [editUser, setEditUser] = useState<EditUser | null>(null);
  const [editTask, setEditTask] = useState<EditTask | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  // Fetch data from the backend API
  useEffect(() => {
    const fetchData = async () => {
      try {
        // In a real app, you would get the API URL from environment variables
        const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';

        // Fetch users
        const usersResponse = await fetch(`${baseUrl}/api/v1/users`);
        if (!usersResponse.ok) throw new Error('Failed to fetch users');
        const usersData = await usersResponse.json();
        setUsers(usersData);

        // Fetch tasks
        const tasksResponse = await fetch(`${baseUrl}/api/v1/tasks`);
        if (!tasksResponse.ok) throw new Error('Failed to fetch tasks');
        const tasksData = await tasksResponse.json();
        setTasks(tasksData);

        setLoading(false);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An unknown error occurred');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Handle creating a new user
  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      console.log('Creating user with data:', newUser); // Debug log
      console.log('Using API URL:', `${baseUrl}/api/v1/users`); // Debug log

      const response = await fetch(`${baseUrl}/api/v1/users`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: newUser.email,
          first_name: newUser.first_name,
          last_name: newUser.last_name,
          password: newUser.password
        }),
      });

      console.log('Response status:', response.status); // Debug log

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText); // Debug log
        throw new Error(`Failed to create user: ${response.status} - ${errorText}`);
      }

      // Refresh the users list
      const userData = await response.json();
      console.log('Created user:', userData); // Debug log
      setUsers([...users, userData]);

      // Reset form
      setNewUser({ email: '', first_name: '', last_name: '', password: '' });
      setError(null); // Clear any previous errors
    } catch (err) {
      console.error('Error creating user:', err); // Debug log
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
        console.error('Network error details:', err);
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while creating user');
      }
    }
  };

  // Handle creating a new task
  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validate that a user is selected
    if (!newTask.user_id) {
      setError('Please select a user for this task');
      return;
    }

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      console.log('Creating task with data:', newTask); // Debug log
      console.log('Using API URL:', `${baseUrl}/api/v1/tasks`); // Debug log

      // Add a timeout to handle potential network delays
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 second timeout

      const response = await fetch(`${baseUrl}/api/v1/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: newTask.title,
          description: newTask.description,
          user_id: newTask.user_id,
          is_completed: newTask.is_completed
        }),
        signal: controller.signal
      });

      clearTimeout(timeoutId);

      console.log('Response status:', response.status); // Debug log

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText); // Debug log
        throw new Error(`Failed to create task: ${response.status} - ${errorText}`);
      }

      // Refresh the tasks list
      const taskData = await response.json();
      console.log('Created task:', taskData); // Debug log
      setTasks([...tasks, taskData]);

      // Reset form
      setNewTask({ title: '', description: '', user_id: '', is_completed: false });
      setError(null); // Clear any previous errors

      // Show success message
      alert(`Task "${newTask.title}" has been added successfully!`);
    } catch (err) {
      console.error('Error creating task:', err); // Debug log
      if (err instanceof TypeError && err.name === 'AbortError') {
        setError('Request timed out. Please check your connection and try again.');
      } else if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
        console.error('Network error details:', err);
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while creating task');
      }
    }
  };

  // Toggle task completion status
  const toggleTaskCompletion = async (taskId: string) => {
    try {
      const task = tasks.find(t => t.id === taskId);
      if (!task) return;

      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      console.log('Toggling task completion for:', taskId); // Debug log

      const response = await fetch(`${baseUrl}/api/v1/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: task.title,
          description: task.description || null,
          is_completed: !task.is_completed,
          user_id: task.user_id
        }),
      });

      console.log('Toggle response status:', response.status); // Debug log

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText); // Debug log
        throw new Error(`Failed to update task: ${response.status} - ${errorText}`);
      }

      // Update the task in the list
      const updatedTask = await response.json();
      console.log('Updated task:', updatedTask); // Debug log
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
      setError(null); // Clear any previous errors
    } catch (err) {
      console.error('Error toggling task:', err); // Debug log
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while updating task');
      }
    }
  };

  // Start editing a user
  const startEditingUser = (user: User) => {
    setEditUser({
      id: user.id,
      email: user.email,
      first_name: user.first_name || '',
      last_name: user.last_name || ''
    });
    setEditingUserId(user.id);
  };

  // Start editing a task
  const startEditingTask = (task: Task) => {
    setEditTask({
      id: task.id,
      title: task.title,
      description: task.description || '',
      user_id: task.user_id,
      is_completed: task.is_completed
    });
    setEditingTaskId(task.id);
  };

  // Cancel editing
  const cancelEditing = () => {
    setEditingUserId(null);
    setEditingTaskId(null);
    setEditUser(null);
    setEditTask(null);
  };

  // Save edited user
  const saveEditedUser = async () => {
    if (!editUser) return;

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${baseUrl}/api/v1/users/${editUser.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          first_name: editUser.first_name,
          last_name: editUser.last_name
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to update user: ${response.status} - ${errorText}`);
      }

      const updatedUser = await response.json();
      setUsers(users.map(u => u.id === editUser.id ? updatedUser : u));
      cancelEditing();
      setError(null);
    } catch (err) {
      console.error('Error updating user:', err);
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while updating user');
      }
    }
  };

  // Save edited task
  const saveEditedTask = async () => {
    if (!editTask) return;

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${baseUrl}/api/v1/tasks/${editTask.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: editTask.title,
          description: editTask.description || null,
          is_completed: editTask.is_completed,
          user_id: editTask.user_id  // This should be the UUID string
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to update task: ${response.status} - ${errorText}`);
      }

      const updatedTask = await response.json();
      setTasks(tasks.map(t => t.id === editTask.id ? updatedTask : t));
      cancelEditing();
      setError(null);
    } catch (err) {
      console.error('Error updating task:', err);
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
        console.error('Network error details:', err);
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while updating task');
      }
    }
  };

  // Delete a user
  const deleteUser = async (userId: string) => {
    if (!window.confirm('Are you sure you want to delete this user?')) return;

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${baseUrl}/api/v1/users/${userId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to delete user: ${response.status} - ${errorText}`);
      }

      setUsers(users.filter(u => u.id !== userId));
      setError(null);
    } catch (err) {
      console.error('Error deleting user:', err);
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while deleting user');
      }
    }
  };

  // Delete a task
  const deleteTask = async (taskId: string) => {
    if (!window.confirm('Are you sure you want to delete this task?')) return;

    try {
      const baseUrl = process.env.BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${baseUrl}/api/v1/tasks/${taskId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to delete task: ${response.status} - ${errorText}`);
      }

      setTasks(tasks.filter(t => t.id !== taskId));
      setError(null);
    } catch (err) {
      console.error('Error deleting task:', err);
      if (err instanceof TypeError && err.message.includes('fetch')) {
        setError('Network error: Unable to connect to the server. Please check if the backend is running and accessible.');
      } else {
        setError(err instanceof Error ? err.message : 'An unknown error occurred while deleting task');
      }
    }
  };

  if (loading) return <div className="loading">Loading your tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <main className="container">
      {/* Cover Section */}
      <section className="cover-section">
        <div className="cover-content">
          <h1 className="cover-title">✨ Todo Dashboard</h1>
          <p className="cover-subtitle">Manage your tasks and users in one place with our modern, intuitive interface</p>

          <div className="stats-container">
            <div className="stat-item">
              <div className="stat-number">{users.length}</div>
              <div className="stat-label">Users</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">{tasks.length}</div>
              <div className="stat-label">Tasks</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">{tasks.filter(t => t.is_completed).length}</div>
              <div className="stat-label">Completed</div>
            </div>
          </div>
        </div>
      </section>

      {/* Tab Navigation */}
      <div className="tabs">
        <button
          className={`tab-button ${activeTab === 'users' ? 'active' : ''}`}
          onClick={() => setActiveTab('users')}
        >
          👥 Users
        </button>
        <button
          className={`tab-button ${activeTab === 'tasks' ? 'active' : ''}`}
          onClick={() => setActiveTab('tasks')}
        >
          ✅ Tasks
        </button>
      </div>

      {/* Add User Form */}
      {activeTab === 'users' && (
        <section className="add-form-section">
          <h2>Add New User</h2>
          <form onSubmit={handleCreateUser} className="add-form">
            <div className="form-group">
              <label htmlFor="firstName">First Name</label>
              <input
                type="text"
                id="firstName"
                value={newUser.first_name}
                onChange={(e) => setNewUser({...newUser, first_name: e.target.value})}
                required
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="lastName">Last Name</label>
              <input
                type="text"
                id="lastName"
                value={newUser.last_name}
                onChange={(e) => setNewUser({...newUser, last_name: e.target.value})}
                required
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={newUser.email}
                onChange={(e) => setNewUser({...newUser, email: e.target.value})}
                required
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={newUser.password}
                onChange={(e) => setNewUser({...newUser, password: e.target.value})}
                required
                className="form-input"
              />
            </div>

            <button type="submit" className="submit-button">Add User</button>
          </form>
        </section>
      )}

      {/* Add Task Form */}
      {activeTab === 'tasks' && (
        <section className="add-form-section">
          <h2>Add New Task</h2>
          <form onSubmit={handleCreateTask} className="add-form">
            <div className="form-group">
              <label htmlFor="title">Title</label>
              <input
                type="text"
                id="title"
                value={newTask.title}
                onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                required
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                value={newTask.description}
                onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                className="form-input textarea"
              />
            </div>

            <div className="form-group">
              <label htmlFor="userId">User ID</label>
              <select
                id="userId"
                value={newTask.user_id}
                onChange={(e) => setNewTask({...newTask, user_id: e.target.value})}
                required
                className="form-input"
              >
                <option value="">Select a user</option>
                {users.map(user => (
                  <option key={user.id} value={user.id}>
                    {user.first_name} {user.last_name} ({user.email})
                  </option>
                ))}
              </select>
            </div>

            <div className="checkbox-group form-group">
              <label htmlFor="isCompleted">Completed?</label>
              <input
                type="checkbox"
                id="isCompleted"
                checked={newTask.is_completed}
                onChange={(e) => setNewTask({...newTask, is_completed: e.target.checked})}
                className="form-checkbox"
              />
            </div>

            <button type="submit" className="submit-button">Add Task</button>
          </form>
        </section>
      )}

      {/* Search Bar */}
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search users or tasks..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
      </div>

      {/* Users Section */}
      {activeTab === 'users' && (
        <section className="users-section">
          <div className="section-header">
            <h2>👥 Users</h2>
            <span className="count-badge">{users.filter(user =>
              user.first_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
              user.last_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
              user.email.toLowerCase().includes(searchTerm.toLowerCase())
            ).length}</span>
          </div>

          {users.filter(user =>
            user.first_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.last_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.email.toLowerCase().includes(searchTerm.toLowerCase())
          ).length === 0 ? (
            <div className="empty-state">
              <p>No users found. Get started by adding some users!</p>
            </div>
          ) : (
            <ul>
              {users.filter(user =>
                user.first_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                user.last_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                user.email.toLowerCase().includes(searchTerm.toLowerCase())
              ).map((user) => (
                <li key={user.id} className="user-card">
                  {editingUserId === user.id && editUser ? (
                    <div className="edit-form">
                      <div className="form-group">
                        <label htmlFor="edit-user-first-name" className="visually-hidden">First Name</label>
                        <input
                          type="text"
                          id="edit-user-first-name"
                          value={editUser.first_name}
                          onChange={(e) => setEditUser({...editUser, first_name: e.target.value})}
                          className="form-input"
                          placeholder="First Name"
                        />
                      </div>
                      <div className="form-group">
                        <label htmlFor="edit-user-last-name" className="visually-hidden">Last Name</label>
                        <input
                          type="text"
                          id="edit-user-last-name"
                          value={editUser.last_name}
                          onChange={(e) => setEditUser({...editUser, last_name: e.target.value})}
                          className="form-input"
                          placeholder="Last Name"
                        />
                      </div>
                      <div className="form-actions">
                        <button onClick={saveEditedUser} className="save-button">Save</button>
                        <button onClick={cancelEditing} className="cancel-button">Cancel</button>
                      </div>
                    </div>
                  ) : (
                    <div className="user-info">
                      <h3>{user.first_name} {user.last_name}</h3>
                      <p className="email">{user.email}</p>
                      <small className="meta">ID: {user.id.substring(0, 8)}...</small>
                      <div className="user-actions">
                        <button onClick={() => startEditingUser(user)} className="edit-button">Edit</button>
                        <button onClick={() => deleteUser(user.id)} className="delete-button">Delete</button>
                      </div>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          )}
        </section>
      )}

      {/* Tasks Section */}
      {activeTab === 'tasks' && (
        <section className="tasks-section">
          <div className="section-header">
            <h2>✅ Tasks</h2>
            <span className="count-badge">{tasks.filter(task =>
              task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
              (task.description && task.description.toLowerCase().includes(searchTerm.toLowerCase()))
            ).length}</span>
          </div>

          {tasks.filter(task =>
            task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
            (task.description && task.description.toLowerCase().includes(searchTerm.toLowerCase()))
          ).length === 0 ? (
            <div className="empty-state">
              <p>No tasks found. Time to be productive!</p>
            </div>
          ) : (
            <ul>
              {tasks.filter(task =>
                task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                (task.description && task.description.toLowerCase().includes(searchTerm.toLowerCase()))
              ).map((task) => (
                <li key={task.id} className={`task-card ${task.is_completed ? 'completed' : ''}`}>
                  {editingTaskId === task.id && editTask ? (
                    <div className="edit-form">
                      <div className="form-group">
                        <label htmlFor="edit-task-title" className="visually-hidden">Title</label>
                        <input
                          type="text"
                          id="edit-task-title"
                          value={editTask.title}
                          onChange={(e) => setEditTask({...editTask, title: e.target.value})}
                          className="form-input"
                          placeholder="Task Title"
                        />
                      </div>
                      <div className="form-group">
                        <label htmlFor="edit-task-description" className="visually-hidden">Description</label>
                        <textarea
                          id="edit-task-description"
                          value={editTask.description}
                          onChange={(e) => setEditTask({...editTask, description: e.target.value})}
                          className="form-input textarea"
                          placeholder="Task Description"
                        />
                      </div>
                      <div className="form-group checkbox-group">
                        <label htmlFor={`edit-task-completed-${task.id}`}>Completed</label>
                        <input
                          type="checkbox"
                          id={`edit-task-completed-${task.id}`}
                          checked={editTask.is_completed}
                          onChange={(e) => setEditTask({...editTask, is_completed: e.target.checked})}
                          className="form-checkbox"
                        />
                      </div>
                      <div className="form-actions">
                        <button onClick={saveEditedTask} className="save-button">Save</button>
                        <button onClick={cancelEditing} className="cancel-button">Cancel</button>
                      </div>
                    </div>
                  ) : (
                    <div className="task-content">
                      <div className="task-header">
                        <h3>{task.title}</h3>
                        <div className="task-actions">
                          <button
                            onClick={() => toggleTaskCompletion(task.id)}
                            className={`toggle-button ${task.is_completed ? 'completed' : 'pending'}`}
                            title={task.is_completed ? 'Mark as incomplete' : 'Mark as complete'}
                          >
                            {task.is_completed ? '✓' : '○'}
                          </button>
                          <button onClick={() => startEditingTask(task)} className="edit-button" title="Edit task">✏️</button>
                          <button onClick={() => deleteTask(task.id)} className="delete-button" title="Delete task">🗑️</button>
                        </div>
                      </div>

                      <p>{task.description || 'No description provided'}</p>

                      <div className="task-meta">
                        <small>User: {task.user_id.substring(0, 8)}...</small>
                        <span className={`status ${task.is_completed ? 'completed' : 'pending'}`}>
                          {task.is_completed ? '✓ Completed' : '⏳ Pending'}
                        </span>
                      </div>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          )}
        </section>
      )}
    </main>
  );
}
