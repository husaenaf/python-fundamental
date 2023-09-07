makan: str = input("Sudah makan belum? ")

match makan:
    case "sudah":
        print("Saya sudah makan")
    case "belum":
        print("Saya belum makan")
    case default:
        print("apa dong")

