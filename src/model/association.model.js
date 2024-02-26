import { User } from './user.model.js';
import { Task } from './task.model.js';

User.hasMany(Task, { foreignKey: 'userId' });
Task.belongsTo(User, { foreignKey: 'userId' });