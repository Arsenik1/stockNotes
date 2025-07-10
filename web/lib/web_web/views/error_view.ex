defmodule WebWeb.ErrorView do
  use WebWeb, :html

  def render("404.html", _assigns), do: "Not Found"
  def render("500.html", _assigns), do: "Internal Server Error"
end
