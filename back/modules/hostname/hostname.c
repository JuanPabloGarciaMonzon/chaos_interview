#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/module.h>
#include <linux/mm.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("GRUPO 28");
MODULE_DESCRIPTION("ACTIVIDAD 2");
MODULE_VERSION("1.0");

static int writefile(struct seq_file* archivo, void *v){
    seq_printf(KERN_HOSTNAME);
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
    printk(KERN_INFO "hola_grupo28\n");
    proc_create("mem_Grupo28", 0, NULL, &ops);
    return 0;
}

static void unload_module(void){
    printk(KERN_INFO "adios_grupo28\n");
    remove_proc_entry("mem_Grupo28", NULL);
}

module_init(load_module);
module_exit(unload_module);