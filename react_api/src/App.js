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
      values: [],
    };
    this.postTest = this.postTest.bind(this);
  }

  postTest() {
    axios
      .post("http://127.0.0.1:8000/postAPI/", {
        a: 3,
        b: 4,
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  componentWillMount() {
    const _this = this;
    axios
      .get("https://5b5e71c98e9f160014b88cc9.mockapi.io/api/v1/lists")
      .then(function (response) {
        console.log(response.data[0]);
        _this.setState({
          values: response.data[0],
        });
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  render() {
    const sidebar = (
      <ul>
        {this.state.values.name}
      </ul>
    );

    return (
      <div>
        <div>
          <button onClick={this.postTest}>post test</button>
        </div>
        {sidebar}
      </div>
    );
  }
}

export default App;
