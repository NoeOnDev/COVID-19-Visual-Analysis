import { DataTypes, Model } from 'sequelize';
import bcrypt from 'bcrypt';
import { sequelize } from '../database/db.config.js';

export class User extends Model {}

User.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    firstName: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    lastName: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    username: {
        type: DataTypes.STRING,
        allowNull: true,
        unique: true,
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true,
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    role: {
        type: DataTypes.ENUM('admin', 'moderator', 'user'),
        allowNull: false,
        defaultValue: 'user',
    },
    verified: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false,
    },
}, {
    sequelize,
    modelName: 'User',
    tableName: 'users',
    paranoid: true,
    timestamps: true,
    underscored: true,
    hooks: {
        beforeCreate: async (user) => {
            const Rounds = 10;
            const salt = await bcrypt.genSalt(Rounds);
            const hash = await bcrypt.hash(user.password, salt);
            user.password = hash;

            const userCount = await User.count();

            if (userCount === 0) {
                user.role = 'admin';
            }
        }
    }
});