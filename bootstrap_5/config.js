const MiniCssExPlugin = require("mini-css-extract-plugin");
module.exports = {
  entry: "./src/js/index.js",
  mode: "development",
  output: {
    filename: "index.js",
    path: "D:/Documents/[WebDev]/DjoleWebSite/website/index/static/bootstrap5/",
  },
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [MiniCssExPlugin.loader, "css-loader", "sass-loader"],
      },
    ],
  },
  plugins: [
    new MiniCssExPlugin({
      filename: "/index.css",
    }),
  ],
};
