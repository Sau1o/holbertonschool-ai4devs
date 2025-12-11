import React, { useState } from 'react';

interface UserCardProps {
    avatarUrl: string;
    name: string;
    bio: string;
    initialIsFollowing: boolean;
}

export const UserCard: React.FC<UserCardProps> = ({ 
    avatarUrl, 
    name, 
    bio, 
    initialIsFollowing 
}) => {
    const [isFollowing, setIsFollowing] = useState<boolean>(initialIsFollowing);

    const handleToggle = () => {
        setIsFollowing(prev => !prev);
    };

    return (
        <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white p-6 border border-gray-200">
            <div className="flex flex-col items-center">
                <img 
                    className="w-24 h-24 rounded-full mb-4 object-cover" 
                    src={avatarUrl} 
                    alt={`${name}'s avatar`} 
                />
                <h2 className="text-xl font-bold mb-2 text-gray-900">{name}</h2>
                <p className="text-gray-700 text-base text-center mb-6">
                    {bio}
                </p>
                
                <button
                    onClick={handleToggle}
                    className={`font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition-colors duration-200 ${
                        isFollowing 
                            ? 'bg-blue-500 hover:bg-blue-700 text-white' 
                            : 'bg-gray-300 hover:bg-gray-400 text-gray-800'
                    }`}
                >
                    {isFollowing ? 'Following' : 'Follow'}
                </button>
            </div>
        </div>
    );
};
