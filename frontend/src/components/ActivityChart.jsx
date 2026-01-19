import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const ActivityChart = ({ data }) => {
  return (
    <div className="chart-card">
      <h2>📊 Last 7 Days Activity</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="active_users" fill="#6366f1" radius={[6, 6, 0, 0]} />
<Bar dataKey="new_users" fill="#f97316" radius={[6, 6, 0, 0]} />

        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ActivityChart;
