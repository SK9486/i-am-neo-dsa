import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

// Book class
class Book {
    private int id;
    private String name;
    private String author;
    private String publisher;
    private int quantity;

    // Default constructor
    Book() {
        this.id = 0;
        this.name = "";
        this.author = "";
        this.publisher = "";
        this.quantity = 0;
    }

    // Parameterized constructor
    Book(int id, String name, String author, String publisher, int quantity) {
        this.id = id;
        this.name = name;
        this.author = author;
        this.publisher = publisher;
        this.quantity = quantity;
    }

    // Getters and Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    // Display book details
    @Override
    public String toString() {
        return "ID: " + id +
               ", Name: " + name +
               ", Author: " + author +
               ", Publisher: " + publisher +
               ", Quantity: " + quantity;
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Book> books = new ArrayList<>();
        Set<String> bookNames = new HashSet<>();

        System.out.print("Enter number of books: ");
        int n = sc.nextInt();
        sc.nextLine(); // consume newline

        // Read book details
        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details of Book " + (i + 1));

            System.out.print("ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Author: ");
            String author = sc.nextLine();

            System.out.print("Publisher: ");
            String publisher = sc.nextLine();

            System.out.print("Quantity: ");
            int quantity = sc.nextInt();
            sc.nextLine();

            Book book = new Book(id, name, author, publisher, quantity);
            books.add(book);
            bookNames.add(name);
        }

        // Display all books
        System.out.println("\nBook Details:");
        for (Book book : books) {
            System.out.println(book);
        }

        // Search book name
        System.out.print("\nEnter book name to search: ");
        String searchName = sc.nextLine();

        if (bookNames.contains(searchName)) {
            System.out.println("Book is present");
        } else {
            System.out.println("Book is not present");
        }

        sc.close();
    }
}
