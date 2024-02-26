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
    done: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false,
    },
}, {
    sequelize,
    modelName: 'Task',
    tableName: 'tasks',
    paranoid: true,
    timestamps: true,
    underscored: true,
});