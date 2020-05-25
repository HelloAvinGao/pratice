import React from "react";
import "./App.css";

const pointArr = [];

let len0 = 25;
for (let i = 0; i < len0; i++) {
  let pointJ = [];
  for (let j = 0; j < len0; j++) {
    pointJ[i + "_" + j] = "0";
  }
  pointArr[i] = pointJ;
}

let width0 = 10;
let height0 = 10;
let isOK = true;

class Test extends React.Component {
  constructor(props) {
    super(props);

    this.initCanvas = this.initCanvas.bind(this);
    this.pointClick = this.pointClick.bind(this);
  }

  // 绘制棋盘
  initCanvas() {
    var contentx = document.getElementById("canvasID");
    var cxt = contentx.getContext("2d");
    contentx.width = len0 * len0 + width0;
    contentx.height = len0 * len0 + height0;
    for (let i = 0; i < len0 + 1; i++) {
      for (let j = 0; j < len0 + 1; j++) {
        cxt.beginPath();
        cxt.moveTo(i * len0 + width0, j * len0 + height0);
        cxt.lineTo((i + 1) * len0 + width0, j * len0 + height0);
        cxt.moveTo(i * len0 + width0, j * len0 + height0);
        cxt.lineTo(i * len0 + width0, (j + 1) * len0 + height0);
        cxt.strokeStyle = "black";
        cxt.stroke();
      }
    }
  }
  // 添加棋子
  pointClick(e) {
    let pointX = Math.round((e.clientX - width0) / len0);
    let pointY = Math.round((e.clientY - height0) / len0);
    if (
      pointArr[pointX][pointX + "_" + pointY] !== 1 &&
      pointArr[pointX][pointX + "_" + pointY] !== 2
    ) {
      if (isOK === true) {
        pointArr[pointX][pointX + "_" + pointY] = 1;
        createPieces(pointX, pointY, isOK);
        isOK = false;
      } else {
        pointArr[pointX][pointX + "_" + pointY] = 2;
        createPieces(pointX, pointY, isOK);
        isOK = true;
      }
    } else {
      return false;
    }
    rules(pointArr);
  }

  componentDidMount() {
    this.initCanvas();
  }

  componentDidUpdate() {
    this.pointClick();
  }

  componentWillUnmount() {}

  render() {
    // width={this.state.width} height={this.state.height}
    return (
      <canvas
        id="canvasID"
        onLoad={this.initCanvas}
        style={{ position: "fixed" }}
        onClick={(event) => this.pointClick(event)}
      ></canvas>
    );
  }
}

function modalClick() {
  (() => {
    // 兼容IE
    if (document.all) {
      document.getElementById("modalClickA").click();
    }
    // 兼容其它浏览器
    else {
      var e = document.createEvent("MouseEvents");
      e.initEvent("click", true, true);
      document.getElementById("modalClickA").dispatchEvent(e);
    }
  })();
}

function createPieces(x, y, isOK) {
  var contentx = document.getElementById("canvasID");
  var cxt = contentx.getContext("2d");
  isOK ? (cxt.fillStyle = "white") : (cxt.fillStyle = "black");
  cxt.beginPath();
  cxt.arc(x * len0 + width0, y * len0 + height0, 5, 0, Math.PI * 2, true);
  cxt.closePath();
  cxt.fill();
}

function rules(array) {
  for (let i = 0; i < array.length; i++) {
    for (var n = 0; n < array.length - 1; n++) {
      if (array[i][i + "_" + n] !== 0 || array[i][i + "_" + n] !== undefined) {
        // 五子为一时
        if (
          (array[i][i + "_" + n] === 1 &&
            array[i + 1][i + 1 + "_" + n] === 1 &&
            array[i + 2][i + 2 + "_" + n] === 1 &&
            array[i + 3][i + 3 + "_" + n] === 1 &&
            array[i + 4][i + 4 + "_" + n] === 1) ||
          (array[i][i + "_" + n] === 2 &&
            array[i + 1][i + 1 + "_" + n] === 2 &&
            array[i + 2][i + 2 + "_" + n] === 2 &&
            array[i + 3][i + 3 + "_" + n] === 2 &&
            array[i + 4][i + 4 + "_" + n] === 2)
        ) {
          console.log("game over");
        }
        // 五子为1时
        if (
          (array[i][i + "_" + n] === 1 &&
            array[i][i + "_" + (n + 1)] === 1 &&
            array[i][i + "_" + (n + 2)] === 1 &&
            array[i][i + "_" + (n + 3)] === 1 &&
            array[i][i + "_" + (n + 4)] === 1) ||
          (array[i][i + "_" + n] === 2 &&
            array[i][i + "_" + (n + 1)] === 2 &&
            array[i][i + "_" + (n + 2)] === 2 &&
            array[i][i + "_" + (n + 3)] === 2 &&
            array[i][i + "_" + (n + 4)] === 2)
        ) {
          console.log("game over");
        }
        // 五子为\时
        if (
          (array[i][i + "_" + n] === 1 &&
            array[i + 1][i + 1 + "_" + (n + 1)] === 1 &&
            array[i + 2][i + 2 + "_" + (n + 2)] === 1 &&
            array[i + 3][i + 3 + "_" + (n + 3)] === 1 &&
            array[i + 4][i + 4 + "_" + (n + 4)] === 1) ||
          (array[i][i + "_" + n] === 2 &&
            array[i + 1][i + 1 + "_" + (n + 1)] === 2 &&
            array[i + 2][i + 2 + "_" + (n + 2)] === 2 &&
            array[i + 3][i + 3 + "_" + (n + 3)] === 2 &&
            array[i + 4][i + 4 + "_" + (n + 4)] === 2)
        ) {
          console.log("game over");
        }
        // 五子为/时
        if (
          (array[i][i + "_" + n] === 1 &&
            array[i + 1][i + 1 + "_" + (n - 1)] === 1 &&
            array[i + 2][i + 2 + "_" + (n - 2)] === 1 &&
            array[i + 3][i + 3 + "_" + (n - 3)] === 1 &&
            array[i + 4][i + 4 + "_" + (n - 4)] === 1) ||
          (array[i][i + "_" + n] === 2 &&
            array[i + 1][i + 1 + "_" + (n - 1)] === 2 &&
            array[i + 2][i + 2 + "_" + (n - 2)] === 2 &&
            array[i + 3][i + 3 + "_" + (n - 3)] === 2 &&
            array[i + 4][i + 4 + "_" + (n - 4)] === 2)
        ) {
          console.log("game over");
        }
      }
    }
  }
}


function App() {
  return <Test className="App"></Test>;
}

export default App;
