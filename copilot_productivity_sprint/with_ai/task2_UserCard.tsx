import React, { useState } from 'react';

interface UserCardProps {
    avatarUrl: string;
    name: string;
    bio: string;
    initialIsFollowing?: boolean;
}

export const UserCard: React.FC<UserCardProps> = ({ avatarUrl, name, bio, initialIsFollowing = false }) => {
    const [isFollowing, setIsFollowing] = useState(initialIsFollowing);

    return (
        <div className="max-w-xs rounded overflow-hidden shadow-lg bg-white border border-gray-200 p-4">
            <img className="w-24 h-24 rounded-full mx-auto" src={avatarUrl} alt={name} />
            <div className="px-6 py-4 text-center">
                <div className="font-bold text-xl mb-2">{name}</div>
                <p className="text-gray-700 text-base">
                    {bio}
                </p>
            </div>
            <div className="px-6 pt-4 pb-2 text-center">
                <button 
                    onClick={() => setIsFollowing(!isFollowing)}
                    className={`px-4 py-2 rounded-full font-semibold text-sm ${
                        isFollowing 
                        ? 'bg-blue-600 text-white hover:bg-blue-700' 
                        : 'bg-gray-300 text-gray-700 hover:bg-gray-400'
                    }`}
                >
                    {isFollowing ? 'Following' : 'Follow'}
                </button>
            </div>
        </div>
    );
};
