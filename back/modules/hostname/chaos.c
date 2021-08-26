#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/module.h>
#include <linux/mm.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("JUAN PABLO GARCÍA MONZÓN");
MODULE_DESCRIPTION("CHAOS_INTERVIEW");
MODULE_VERSION("1.0");

static int writefile(struct seq_file* archivo, void *v){
    struct sysinfo inf;
    si_meminfo(&inf);
    seq_printf(archivo, "Uptime: %lu MB\n", inf.uptime);
    seq_printf(archivo, "1: %lu MB\n", inf.loads[1]);
    seq_printf(archivo, "5: %lu MB\n", inf.loads[2]);
    seq_printf(archivo, "15: %lu MB\n", inf.loads[3]);
    return 0;
}

static int atOpen(struct inode* inodo, struct file* file){
    return single_open(file, writefile, NULL);
}

static struct file_operations ops = {
    .open = atOpen,
    .read = seq_read
};

static int load_module(void){
    printk(KERN_INFO "Hi_chaos\n");
    proc_create("chaos", 0, NULL,&ops);
    return 0;
}

static void unload_module(void){
    printk(KERN_INFO "Gby_chaos\n");
    remove_proc_entry("chaos", NULL);
}

module_init(load_module);
module_exit(unload_module);