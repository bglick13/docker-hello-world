import './App.css';
import React from 'react';
import axios from "axios";

function App() {
  const initialState = {
    server_ip: "",
    server_port: "",
    client_ip: "",
    client_port: "",
    host: ""
  }
  const [state, setState] = React.useState(initialState)

  const fetchIp = () => {
    axios.get("http://localhost:8080/whats_my_ip").then((res) => {
      console.log(res)
      setState(res.data)
    })
  }

  return (
    <div className="App">
      <p>{`Server IP: ${state.server_ip}`}</p>
      <p>{`Server Port: ${state.server_port}`}</p>
      <p>{`Client IP: ${state.client_ip}`}</p>
      <p>{`Client Port: ${state.client_port}`}</p>
      <p>{`Host: ${state.host}`}</p>
      <button onClick={fetchIp}>Whats my IP</button>
    </div>
  );
}

export default App;
