const ActiveUsers = ({ users }) => {
  return (
    <div className="users-card">
      <h2>🔥 Active ≥ 4 Days (Last 7 Days)</h2>
      {users.length === 0 ? (
        <p>No highly active users found</p>
      ) : (
        <ul>
          {users.map((user) => (
            <li key={user}>{user}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ActiveUsers;
