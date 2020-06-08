import React from "react";
import "./App.css";
import {
  AxiosProvider,
  Request,
  Get,
  Delete,
  Head,
  Post,
  Put,
  Patch,
  withAxios,
} from "react-axios";
import axios from "axios";

const url1 = "https://api.github.com/users/github";
const url2 = "https://5b5e71c98e9f160014b88cc9.mockapi.io/api/v1/lists";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],
      isLoaded: false,
    };
  }

  componentWillMount() {
    const _this=this;
    axios
      .get(url2)
      .then(function (response) {
        console.log(response.data);
        _this.setState({
          users:response.data,
          isLoaded:true
        })
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  render() {
    if (!this.state.isLoaded) {
      return <div>Loading</div>;
    } else {
      return (
        <table className="table table-bordered">
          <thead>
            <tr>
              <th className="text-center">ID</th>
              <th className="text-center">姓名</th>
              <th className="text-center">年龄</th>
              <th className="text-center">性别</th>
            </tr>
          </thead>
          <tbody>
            <TrData users={this.state.users}/>
          </tbody>
        </table>
      );
    }
  }
}

class TrData extends React.Component{
  constructor(props){
    super(props);
  }
  render(){
    return (
      this.props.users.map((user,i)=>{
          return (
              <tr key={user.id} className="text-center">
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.age}</td>
                <td>{user.sex}</td>
              </tr>
          )       
      })
    )
  }
}

export default App;
