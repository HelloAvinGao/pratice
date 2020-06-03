import React from "react";
import "./App.css";

const len = 25;
const maps = [];
for (let i = 0; i <= len; i++) {
  let tempList = {};
  for (let j = 0; j <= len; j++) {
    tempList[i + "_" + j] = 0;
  }
  maps[i] = tempList;
}

const canvasProps = {
  width: len * len,
  height: len * len,
};

class Website extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Maps: maps,
      canvasProps: canvasProps,
      isOK: true,
    };
  }

  componentDidMount() {
    this.createBoard();
  }

  // componentDidUpdate() {
  //   this.rules();
  // }

  rules(array) {
    for (let i = 0; i < array.length; i++) {
      for (let j = 0; j < array.length; j++) {
        if (array[j][j + "_" + i] !== 0) {
          // 五子为|时
          if (
            (array[j][j + "_" + i] === 1 &&
              array[j + 1][j + 1 + "_" + i] === 1 &&
              array[j + 2][j + 2 + "_" + i] === 1 &&
              array[j + 3][j + 3 + "_" + i] === 1 &&
              array[j + 4][j + 4 + "_" + i] === 1) ||
            (array[j][j + "_" + i] === 2 &&
              array[j + 1][j + 1 + "_" + i] === 2 &&
              array[j + 2][j + 2 + "_" + i] === 2 &&
              array[j + 3][j + 3 + "_" + i] === 2 &&
              array[j + 4][j + 4 + "_" + i] === 2)
          ) {
            console.log("game over");
          }
          // 五子为-时
          if (
            (array[j][j + "_" + i] === 1 &&
              array[j][j + "_" + (i + 1)] === 1 &&
              array[j][j + "_" + (i + 2)] === 1 &&
              array[j][j + "_" + (i + 3)] === 1 &&
              array[j][j + "_" + (i + 4)] === 1) ||
            (array[j][j + "_" + i] === 2 &&
              array[j][j + "_" + (i + 1)] === 2 &&
              array[j][j + "_" + (i + 2)] === 2 &&
              array[j][j + "_" + (i + 3)] === 2 &&
              array[j][j + "_" + (i + 4)] === 2)
          ) {
            console.log("game over");
          }
          // 五子为\时
          if (
            (array[j][j + "_" + i] === 1 &&
              array[j + 1][j + 1 + "_" + (i + 1)] === 1 &&
              array[j + 2][j + 2 + "_" + (i + 2)] === 1 &&
              array[j + 3][j + 3 + "_" + (i + 3)] === 1 &&
              array[j + 4][j + 4 + "_" + (i + 4)] === 1) ||
            (array[j][j + "_" + i] === 2 &&
              array[j + 1][j + 1 + "_" + (i + 1)] === 2 &&
              array[j + 2][j + 2 + "_" + (i + 2)] === 2 &&
              array[j + 3][j + 3 + "_" + (i + 3)] === 2 &&
              array[j + 4][j + 4 + "_" + (i + 4)] === 2)
          ) {
            console.log("game over");
          }
          // 五子为/时
          if (
            (array[j][j + "_" + i] === 1 &&
              array[j + 1][(j + 1) + "_" + (i - 1)] === 1 &&
              array[j + 2][(j + 2) + "_" + (i - 2)] === 1 &&
              array[j + 3][(j + 3) + "_" + (i - 3)] === 1 &&
              array[j + 4][(j + 4) + "_" + (i - 4)] === 1) ||
            (array[j][j + "_" + i] === 2 &&
              array[j + 1][(j + 1) + "_" + (i - 1)] === 2 &&
              array[j + 2][(j + 2) + "_" + (i - 2)] === 2 &&
              array[j + 3][(j + 3) + "_" + (i - 3)] === 2 &&
              array[j + 4][(j + 4) + "_" + (i - 4)] === 2)
          ) {
            console.log("game over");
          }
        }
      }
    }
  }

  createPiece = (event) => {
    const e = event || window.event;
    const scrollX =
      document.documentElement.scrollLeft || document.body.scrollLeft;
    const scrollY =
      document.documentElement.scrollTop || document.body.scrollTop;
    const x = e.pageX || e.clientX + scrollX;
    const y = e.pageY || e.clientY + scrollY;
    const i = Math.round(x / len);
    const j = Math.round(y / len);
    let coordinate = j + "_" + i;

    var c = document.getElementById("checkerboard");
    var ctx = c.getContext("2d");
    if (this.state.isOK) {
      ctx.fillStyle = "white";
      this.setState({
        isOK: false,
      });
      maps[j][coordinate] = 1;
    } else {
      ctx.fillStyle = "black";
      this.setState({
        isOK: true,
      });
      maps[j][coordinate] = 2;
    }

    ctx.beginPath();
    ctx.arc(i * len, j * len, 10, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    this.rules(maps);
  };

  createBoard = () => {
    const c = document.getElementById("checkerboard");
    const ctx = c.getContext("2d");
    for (let i = 0; i <= len; i++) {
      for (let j = 0; j <= len; j++) {
        ctx.moveTo(i * len, j * len);
        ctx.lineTo(i * len, (j + 1) * len);
        ctx.stroke();
        ctx.moveTo(i * len, j * len);
        ctx.lineTo((i + 1) * len, j * len);
        ctx.stroke();
      }
    }
  };

  render() {
    return (
      <div>
        <canvas
          id="checkerboard"
          onClick={this.createPiece}
          width={this.state.canvasProps.width}
          height={this.state.canvasProps.height}
          style={{ border: "1px solid blue" }}
        ></canvas>
      </div>
    );
  }
}

function App() {
  return <Website />;
}

export default App;
