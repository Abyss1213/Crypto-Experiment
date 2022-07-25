public class LockExample1{
    public static final boolean EXCLUSIVE = false;
    public static final boolean SHARD = true;

    public static void main(String args[]) throws IOException{
        FileLock sharedLock = null;
        FileLock exclusiveLock = null;
        try{
            RandomAccessFile raf = new RandomAccessFile("file.txt","rw");
            byte[] buffer = new byte[2];
            int len = 0;
            while((len = raf.read(buffer, 0, 2)) != -1){
                System.out.print(new String(buffer, 0, len));
}
}
}
}