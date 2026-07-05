public class server {
    public static void main (String[] args){
        SkeletonImpl del = new SkeletonImpl();
        Skeleton sk = new Skeleton(del, 0);
        sk.run_skeleton();
    }
}
