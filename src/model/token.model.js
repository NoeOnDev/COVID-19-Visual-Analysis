import { DataTypes, Model } from 'sequelize';
import { sequelize } from '../database/db.config.js';

export class Token extends Model {}

Token.init({
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    token: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    userId: {
        type: DataTypes.INTEGER,
        references: {
            model: 'users',
            key: 'id',
        },
        allowNull: false,
    },
}, {
    sequelize,
    modelName: 'VerificationToken',
    tableName: 'verification_tokens',
    timestamps: true,
    underscored: true,
    freezeTableName: true,
});