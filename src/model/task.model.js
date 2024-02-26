import { DataTypes, Model } from 'sequelize';
import { sequelize } from '../database/db.config.js';

export class Task extends Model {}

Task.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    title: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    description: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    timeSpent: {
        type: DataTypes.INTEGER,
        allowNull: true,
        defaultValue: 0,
    },
    status: {
        type: DataTypes.ENUM('pending', 'started', 'completed'),
        allowNull: false,
        defaultValue: 'pending',
    },
    done: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false,
    },
    userId: {
        type: DataTypes.INTEGER,
        references: {
            model: 'users',
            key: 'id'
        },
        allowNull: false,
    }
}, {
    sequelize,
    modelName: 'Task',
    tableName: 'tasks',
    paranoid: true,
    timestamps: true,
    underscored: true,
});