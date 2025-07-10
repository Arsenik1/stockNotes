defmodule WebWeb.NotesLive do
  use WebWeb, :live_view

  @impl true
  def mount(_params, _session, socket) do
    {:ok, assign(socket, date: Date.utc_today(), mode: :short, note: "", stock: "")}
  end

  @impl true
  def handle_event("set_date", %{"date" => date}, socket) do
    {:noreply, assign(socket, :date, date)}
  end

  def handle_event("set_mode", %{"mode" => mode}, socket) do
    {:noreply, assign(socket, :mode, String.to_atom(mode))}
  end

  def handle_event("add_stock", %{"stock" => stock}, socket) do
    stock = String.upcase(stock)
    File.mkdir_p!("short_term")
    File.mkdir_p!("long_term")
    for dir <- ["short_term", "long_term"] do
      path = Path.join(dir, stock <> ".txt")
      unless File.exists?(path) do
        File.write!(path, "Notes for #{stock}\n\n")
      end
    end
    {:noreply, socket}
  end

  def handle_event("add_note", %{"stock" => stock, "note" => note}, socket) do
    stock = String.upcase(stock)
    dir = if socket.assigns.mode == :short, do: "short_term", else: "long_term"
    path = Path.join(dir, stock <> ".txt")
    File.write!(path, "#{socket.assigns.date}: #{note}\n", [:append])
    {:noreply, socket}
  end

  def handle_event("read_notes", %{"stock" => stock}, socket) do
    stock = String.upcase(stock)
    short = Path.join("short_term", stock <> ".txt")
    long = Path.join("long_term", stock <> ".txt")
    notes =
      [short, long]
      |> Enum.map(fn path ->
        if File.exists?(path), do: File.read!(path), else: ""
      end)
      |> Enum.join("\n----\n")
    {:noreply, assign(socket, :notes, notes)}
  end

  @impl true
  def render(assigns) do
    ~H"""
    <h2>Stock Notes</h2>
    <form phx-submit="set_date">
      <input type="date" name="date" value={@date} />
      <button type="submit">Set Default Date</button>
    </form>

    <form phx-submit="set_mode">
      <select name="mode">
        <option value="short" selected={@mode == :short}>Short</option>
        <option value="long" selected={@mode == :long}>Long</option>
      </select>
      <button type="submit">Switch Mode</button>
    </form>

    <form phx-submit="add_stock">
      <input type="text" name="stock" placeholder="Stock code" />
      <button type="submit">Add Stock</button>
    </form>

    <form phx-submit="add_note">
      <input type="text" name="stock" placeholder="Stock code" />
      <input type="text" name="note" placeholder="Note" />
      <button type="submit">Add Note</button>
    </form>

    <form phx-submit="read_notes">
      <input type="text" name="stock" placeholder="Stock code" />
      <button type="submit">Read Notes</button>
    </form>

    <pre><%= @notes %></pre>
    """
  end
end
